import sys
import os
import time
import re
import urllib2
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

items.append(Item("Ryobi Orbital Sander - Home Depot", \
                  "https://www.homedepot.com/p/Ryobi-18-Volt-ONE-5-in-Cordless-Random-Orbit-Sander-Tool-Only-P411/205975756", \
                  "itemprop"))
items.append(Item("S&W M&P 22LR Pistol - KY Gun Co", \
                  "https://kygunco.com/Product/View?ItemNo=101022", \
                  "itemprop"))
items.append(Item("S&W M&P 22LR Pistol - Academy", \
                  "https://www.academy.com/shop/pdp/smith-wesson-m-p-22-lr-compact-pistol", \
                  "itemprop"))
items.append(Item("S&W M&P 22LR Pistol - Buds Gun Shop", \
                  "https://www.budsgunshop.com/catalog/product_info.php/cPath/2084_2108/products_id/93813/S%26W+M%26P22+22LR+COMP+3.6+10R+Black", \
                  "itemprop"))


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
    except:
        log.log_info(" - " + item.name + " ... Error reading url:" + item.url)
        continue
    soup = BeautifulSoup(content, "html.parser")
    if item.html_element == "itemprop":
        price = soup.find_all("span", itemprop="price")
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
    msg = MIMEText(log.get_log())
    msg['Subject'] = "Message from PriceCheck.py"
    msg['From'] = email_address
    msg['To'] = email_address
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

log.log_info(' ')

