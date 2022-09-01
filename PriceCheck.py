import sys
import os
import time
import json
import re
import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
from bs4 import BeautifulSoup
import smtplib
from ConsoleLogger import ConsoleLogger
from StringBuilderLogger import StringBuilderLogger
from Item import Item


# Enter your SimplePush key below (see https://simplepush.io/)
SIMPLE_PUSH_KEY = ""


log = ConsoleLogger(None)

# Comment the following line to disable email notification
log = StringBuilderLogger(log)


NUM_RETRIES = 1
#NUM_RETRIES = 5
RETRY_DELAY_SECONDS = 2
#RETRY_DELAY_SECONDS = 30

email_address = "your@email.com"
email_addresses = ["your@email.com"]

DIVIDER = "----------------------------------------------------------"

message = ""


price_regex = re.compile(r'EVO.151...price..\d\d\d\.\d\d')

# List of items to search for prices
items = []

items.append(Item("Rome Reverb Rocker at EVO", "https://www.evo.com/outlet/snowboards/rome-reverb-rocker-se-snowboard", "script"))
items.append(Item("Divinity: Original Sin 2", "https://store.steampowered.com/app/435150/Divinity_Original_Sin_2__Definitive_Edition/", "steam"))
items.append(Item("Age of Empires II: Definitive Edition", "https://store.steampowered.com/app/813780/Age_of_Empires_II_Definitive_Edition/", "steam"))
#items.append(Item("Ryobi Orbital Sander - Home Depot", "https://www.homedepot.com/p/Ryobi-18-Volt-ONE-5-in-Cordless-Random-Orbit-Sander-Tool-Only-P411/205975756", "itemprop"))


print(str(sys.argv))
if len(sys.argv) > 1:
    email_address = sys.argv[1]
else:
    email_address = ""

log.log_info("Price check...\n")


def try_function(a_function):
    """ Try to run the function and retry upon failure for NUM_RETRIES times """
    for i in range (NUM_RETRIES):
        if a_function() == True:
            break
        time.sleep(RETRY_DELAY_SECONDS)


for item in items:
    content = ""
    try:
        print("\nRequesting ", item.name)
        response = requests.get(item.url, timeout=3)
        response.raise_for_status()
        content = response.text
    except HTTPError as http_err:
        log.log_info(" - " + item.name + " ... HTTP Error reading url: " + str(http_err))
        continue
    except Timeout:
        log.log_info(" - " + item.name + " ... The request timed out")
        continue
    except Exception as ex:
        log.log_info(" - " + item.name + " ... Error reading url: " + str(ex))
        continue
    soup = BeautifulSoup(content, "html.parser")
    if item.html_element == "itemprop":
        price = soup.find_all("span", itemprop="price")
    elif item.html_element == "script":
        product_schema = soup.find_all(id="product-schema")
        if product_schema:
            for prod in product_schema:
                price_str = price_regex.search(str(prod))
                price = price_str.group()
    elif item.html_element == "steam":
        price = soup.find(class_="game_purchase_price")
    elif item.html_element == "priceblock_ourprice":
        price = soup.find_all("span", id="priceblock_ourprice")
    elif item.html_element == "content":
        #pattern = re.compile('sup.\d\d.\d\d..span',re.DOTALL)
        #pattern = re.compile('\d\d\.\d\d', re.DOTALL)
        pattern = re.compile('font jumbo strong', re.DOTALL)
        price = re.findall(pattern, content)
        for pp in price:
            log.log_info(pp)
    else:
        price = soup.find_all(item.html_element)
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info(" - " + item.name + " ... Price: %s" % match.group(0))
    else:
        log.log_info(" - " + item.name + " ... Error retrieving price")


#log.log_info(DIVIDER)


# Use SimplePush
if SIMPLE_PUSH_KEY is not "":
    msg = log.get_log()
    push_url = "https://api.simplepush.io/send/" + SIMPLE_PUSH_KEY + "/" + "Price Check/" + msg
    print("\nSending notification...\n" + push_url)
    response = requests.get(push_url, timeout=8)


# Set to True to send email with results
if email_address != "":
    log.log_info("\nSending mail to " + email_address + "...")
    msg = log.get_log()
    msg = "From: " + email_address + "\n"
    msg += "To " + email_address + "\n"
    msg += "Subject: Message from PriceCheck.py\n\n"
    msg += log.get_log()
    try:
        s = smtplib.SMTP('localhost')
        s.sendmail(email_address, email_addresses, msg)
        s.quit()

        log_msg = log.get_log()
        if log_msg != "":
            log_msg = log_msg.replace("\"", "\\\"")
            log_msg = log_msg.replace("\(", "\\\(")
            log_msg = log_msg.replace("\$", "\\\$")
            cmd = "echo \"" + log_msg + "\" | mail -s \"Message from PriceCheck.py\" " + email_address
            os.system(cmd)

    except Exception as ex:
        log.log_info("\n  Error sending mail: " + str(ex))

log.log_info(' ')

