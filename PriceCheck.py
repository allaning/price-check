import sys
import os
import re
from bs4 import BeautifulSoup
import urllib2
import smtplib
from email.mime.text import MIMEText
from ConsoleLogger import ConsoleLogger
from StringBuilderLogger import StringBuilderLogger

log = ConsoleLogger(None)
log = StringBuilderLogger(log)

email_address = "your@email.com"
divider = "----------------------------------------------------------"
message = ""

print str(sys.argv)
if len(sys.argv) > 1:
    email_address = sys.argv[1]
else:
    print("Usage: python PriceCheck.py your@emailaddress.com")
    exit()

log.logInfo("Price check...\n")

if True:
    log.logInfo(divider)
    log.logInfo('Merrell Moab Ventilator Wide')
    url = "http://www.merrell.com/US/en/moab-ventilator-wide-width/16220M.html"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("span", class_="promo-price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.logInfo("     SALE: %s" % match.group(0))
    else:
        price = soup.find_all("span", itemprop="price")
        match = re.search("\d+\.\d\d", str(price))
        if match != None:
            log.logInfo("     %s" % match.group(0))
        else:
            log.logInfo("  Error retrieving price.")
    log.logInfo('     (80 = target price)')

if True:
    log.logInfo(divider)
    log.logInfo('Nebraska Furniture Mart Polk 12" sub')
    url = "https://www.nfm.com/DetailsPage.aspx?productid=31539166"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("div", class_="yourprice")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.logInfo("     %s" % match.group(0))
    else:
        log.logInfo("  Error retrieving price.")
    log.logInfo('     (270 = target price)')

log.logInfo(divider)

if False:
    msg = MIMEText(log.getLog())
    msg['Subject'] = "Message from PriceCheck.py"
    msg['From'] = email_address
    msg['To'] = email_address
    s = smtplib.SMTP('localhost')
    s.sendmail(email_address, email_address, msg.as_string())
    s.quit()

if True:
    filteredLog = log.getLog()
    filteredLog = filteredLog.replace("\"", "\\\"")
    filteredLog = filteredLog.replace("\(", "\\\(")
    filteredLog = filteredLog.replace("\$", "\\\$")
    cmd = "echo \"" + filteredLog + "\" | mail -s \"Message from PriceCheck.py\" " + email_address
    os.system(cmd)

