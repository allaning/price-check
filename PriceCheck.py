import sys
import os
import time
import re
import urllib2
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from ConsoleLogger import ConsoleLogger
from StringBuilderLogger import StringBuilderLogger
from Item import Item


log = ConsoleLogger(None)

# Comment the following line to disable email notification
#log = StringBuilderLogger(log)


NUM_RETRIES = 1
#NUM_RETRIES = 5
RETRY_DELAY_SECONDS = 2
#RETRY_DELAY_SECONDS = 30

email_address = "your@email.com"
divider = "----------------------------------------------------------"
message = ""


# List of items to search for prices
items = []

items.append(Item("Ryobi Orbital Sander - Home Depot", "https://www.homedepot.com/p/Ryobi-18-Volt-ONE-5-in-Cordless-Random-Orbit-Sander-Tool-Only-P411/205975756", "itemprop"))
items.append(Item("3-Shelf - Home Depot", "https://www.homedepot.com/p/HDX-30-3-in-H-x-24-in-W-x-14-in-D-3-Shelf-Wire-Black-Shelving-Unit-31424BPS/302073746", "itemprop"))
items.append(Item("3-Shelf - Lowes", "https://www.lowes.com/pd/Style-Selections-30-5-in-H-x-23-in-W-x-13-4-in-D-3-Tier-Steel-Freestanding-Shelving-Unit/999990400", "content"))
items.append(Item("4-Shelf Plastic - Lowes", "https://www.lowes.com/pd/Blue-Hawk-48-in-H-x-22-in-W-x-14-25-in-D-4-Tier-Plastic-Freestanding-Shelving-Unit/1000017489", "content"))
items.append(Item("4-Shelf Plastic (Larger) - Lowes", "https://www.lowes.com/pd/Blue-Hawk-56-5-in-H-x-36-in-W-x-24-in-D-4-Tier-Plastic-Freestanding-Shelving-Unit/3344676", "content"))
items.append(Item("4-Shelf Steel (Larger) - Lowes", "https://www.lowes.com/pd/Style-Selections-53-in-H-x-35-7-in-W-x-14-in-D-4-Tier-Steel-Freestanding-Shelving-Unit/999990402", "content"))
items.append(Item("Ledger Nano S - Amazon", "https://smile.amazon.com/gp/product/B01J66NF46/", "priceblock_ourprice"))


print str(sys.argv)
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
        content = urllib2.urlopen(item.url).read()
    except Exception:
        try:
            page = requests.get(item.url)
            content = page.text
        except Exception as ex:
            log.log_info(" - " + item.name + " ... Error reading url: " + str(ex))
            continue
    soup = BeautifulSoup(content, "html.parser")
    if item.html_element == "itemprop":
        price = soup.find_all("span", itemprop="price")
    elif item.html_element == "priceblock_ourprice":
        price = soup.find_all("span", id="priceblock_ourprice")
    elif item.html_element == "content":
        #pattern = re.compile('sup.\d\d.\d\d..span',re.DOTALL)
        #pattern = re.compile('\d\d\.\d\d', re.DOTALL)
        pattern = re.compile('font jumbo strong', re.DOTALL)
        price = re.findall(pattern, content)
        #aing log.log_info(str(soup))
        for pp in price:
            log.log_info(pp) #aing
    else:
        price = soup.find_all(item.html_element)
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info(" - " + item.name + " ... Price: %s" % match.group(0))
    else:
        log.log_info(" - " + item.name + " ... Error retrieving price")


#log.log_info(divider)

# Set to True to send email with results
if email_address != "":
    log.log_info("\nSending mail to " + email_address + "...")
    msg = MIMEText(log.get_log())
    msg['Subject'] = "Message from PriceCheck.py"
    msg['From'] = email_address
    msg['To'] = email_address
    try:
        s = smtplib.SMTP('localhost')
        s.sendmail(email_address, email_address, msg.as_string())
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

