import sys
import os
import time
import re
from bs4 import BeautifulSoup
import urllib2
import smtplib
from email.mime.text import MIMEText
from ConsoleLogger import ConsoleLogger
from StringBuilderLogger import StringBuilderLogger


log = ConsoleLogger(None)

# Comment the following line to disable email notification
log = StringBuilderLogger(log)


NUM_RETRIES = 5
RETRY_DELAY_SECONDS = 30

email_address = "your@email.com"
divider = "----------------------------------------------------------"
message = ""


def try_function(a_function):
    """ Try to run the function and retry upon failure for NUM_RETRIES times """
    for i in range (NUM_RETRIES):
        if a_function() == True:
            break
        time.sleep(RETRY_DELAY_SECONDS)


print str(sys.argv)
if len(sys.argv) > 1:
    email_address = sys.argv[1]
else:
    print("Usage: python PriceCheck.py your@emailaddress.com")
    exit()

log.log_info("Price check...\n")


# Subwoofers

def bic_v1220_1():
    log.log_info(divider)
    log.log_info('BIC V1220 12" Down Firing Subwoofer')
    log.log_info('     (180 = target price)')
    url = "http://www.bestbuy.com/site/bic-america-12-430-watt-powered-subwoofer/2750541.p?id=1218348487515&skuId=2750541"
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
        log.log_info("     Error retrieving price - Best Buy")
        return False
    return True

try_function(bic_v1220_1)

def bic_v1220_2():
    url = "http://www.newegg.com/Product/Product.aspx?Item=N82E16882007001"
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
        log.log_info("     Error retrieving price - Newegg.com")
        return False
    return True

try_function(bic_v1220_2)

def bic_f12_1():
    log.log_info(divider)
    log.log_info('BIC F12 12" Front Firing Subwoofer')
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
        log.log_info("     Error retrieving price - Best Buy")
        return False
    return True

try_function(bic_f12_1)

def bic_f12_2():
    url = "http://www.newegg.com/Product/Product.aspx?Item=N82E16886986001"
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
        log.log_info("     Error retrieving price - Newegg.com")
        return False
    return True

try_function(bic_f12_2)

def bic_f12_3():
    url = "https://www.amazon.com/BIC-America-F12-475-Watt-Subwoofer/dp/B0015A8Y5M"
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
        log.log_info("     Error retrieving price - Amazon.com")
        return False
    return True

try_function(bic_f12_3)

def polk_psw505_1():
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
        log.log_info("     Error retrieving price - Newegg.com")
        return False
    return True

try_function(polk_psw505_1)

def polk_psw505_2():
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
        log.log_info("     Error retrieving price - Amazon.com")
        return False
    return True

try_function(polk_psw505_2)

def polk_psw125_1():
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
        log.log_info("     Error retrieving price - Nebraska Furniture Mart")
        return False
    return True

try_function(polk_psw125_1)

def polk_psw125_2():
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
        log.log_info("     Error retrieving price - Amazon.com")
        return False
    return True

try_function(polk_psw125_2)


# Misc

def wavemaster_1():
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
        log.log_info("     Error retrieving price - Dick\'s Sporting Goods")
        return False
    return True

try_function(wavemaster_1)


log.log_info(divider)

if False:
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

