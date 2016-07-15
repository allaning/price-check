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

log.log_info("Price check...\n")


# Merrell shoes

if True:
    log.log_info(divider)
    log.log_info('Merrell Moab Ventilator Wide')
    log.log_info('     (80 = target price)')
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
        log.log_info("     SALE: %s - Merrell.com" % match.group(0))
    else:
        price = soup.find_all("span", itemprop="price")
        match = re.search("\d+\.\d\d", str(price))
        if match != None:
            log.log_info("     %s - Merrell.com" % match.group(0))
        else:
            log.log_info("  Error retrieving price.")

if True:
    url = "http://www.dickssportinggoods.com/product/index.jsp?productId=2979956"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("span", itemprop="price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     %s - Dick\'s Sporting Goods" % match.group(0))
    else:
        log.log_info("  Error retrieving price - Dick\'s Sporting Goods")

if True:
    url = "https://www.rei.com/product/748515/merrell-moab-ventilator-hiking-shoes-mens"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("span", itemprop="price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     %s - REI" % match.group(0))
    else:
        log.log_info("  Error retrieving price - REI")


if True:
    log.log_info(divider)
    log.log_info('Merrell FST Wide')
    log.log_info('     (90 = arbitrary target price)')
    url = "http://www.merrell.com/US/en/moab-fst-wide-width/24839M.html"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("span", class_="promo-price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     SALE: %s - Merrell.com" % match.group(0))
    else:
        price = soup.find_all("span", itemprop="price")
        match = re.search("\d+\.\d\d", str(price))
        if match != None:
            log.log_info("     %s - Merrell.com" % match.group(0))
        else:
            log.log_info("  Error retrieving price.")


# Subwoofers

if True:
    log.log_info(divider)
    log.log_info('BIC F12 12" Subwoofer')
    log.log_info('     (210 = arbitrary target price)')
    url = "http://www.bestbuy.com/site/bic-america-formula-12-475w-powered-subwoofer-black/4235056.p?id=1218463773881&skuId=4235056"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("div", class_="item-price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     %s - Best Buy" % match.group(0))
    else:
        log.log_info("  Error retrieving price - Best Buy")

if True:
    log.log_info(divider)
    log.log_info('Polk PSW505 12" Subwoofer')
    log.log_info('     (124 = target price)')
    url = "http://www.newegg.com/Product/Product.aspx?Item=N82E16882290130"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("meta", itemprop="price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     %s - Newegg.com" % match.group(0))
    else:
        log.log_info("  Error retrieving price - Newegg.com")

if True:
    url = "https://www.amazon.com/Polk-Audio-12-Inch-Powered-Subwoofer/dp/B000092TT0"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("span", id="priceblock_dealprice")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     %s - Amazon.com" % match.group(0))
    else:
        log.log_info("  Error retrieving price - Amazon.com")

if True:
    log.log_info(divider)
    log.log_info('Polk PSW125 12" Subwoofer')
    log.log_info('     (265 = target price)')
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
        log.log_info("     %s - Nebraska Furniture Mart" % match.group(0))
    else:
        log.log_info("  Error retrieving price - Nebraska Furniture Mart")

if True:
    url = "https://www.amazon.com/Polk-Audio-12-Inch-Powered-Subwoofer/dp/B000OY6CVI"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("span", id="priceblock_ourprice")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     %s - Amazon.com" % match.group(0))
    else:
        log.log_info("  Error retrieving price - Amazon.com")


# Misc

if True:
    log.log_info(divider)
    log.log_info('Century Wavemaster')
    url = "http://www.dickssportinggoods.com/product/index.jsp?productId=12447161"
    content = ""
    try:
        content = urllib2.urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup(content)
    price = soup.find_all("span", itemprop="price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        log.log_info("     %s - Dick\'s Sporting Goods" % match.group(0))
    else:
        log.log_info("  Error retrieving price - Dick\'s Sporting Goods")

log.log_info(divider)

if False:
    msg = MIMEText(log.get_log())
    msg['Subject'] = "Message from PriceCheck.py"
    msg['From'] = email_address
    msg['To'] = email_address
    s = smtplib.SMTP('localhost')
    s.sendmail(email_address, email_address, msg.as_string())
    s.quit()

if True:
    filteredLog = log.get_log()
    filteredLog = filteredLog.replace("\"", "\\\"")
    filteredLog = filteredLog.replace("\(", "\\\(")
    filteredLog = filteredLog.replace("\$", "\\\$")
    cmd = "echo \"" + filteredLog + "\" | mail -s \"Message from PriceCheck.py\" " + email_address
    os.system(cmd)

