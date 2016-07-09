from bs4 import BeautifulSoup
import urllib2
import re

divider = "====================================================================================="

print("Price check...\n")

if True:
    print(divider)
    print('Merrell Moab Ventilator Wide (Target $80)')
    url = "http://www.merrell.com/US/en/moab-ventilator-wide-width/16220M.html"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    price = soup.find_all("span", class_="promo-price")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        print("  SALE: $%s" % match.group(0))
    else:
        price = soup.find_all("span", itemprop="price")
        match = re.search("\d+\.\d\d", str(price))
        if match != None:
            print("  Regular Price: $%s" % match.group(0))
        else:
            print("  Error retrieving price.")

if True:
    print(divider)
    print('Nebraska Furniture Mart Polk 12" sub (Target $270)')
    url = "https://www.nfm.com/DetailsPage.aspx?productid=31539166"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    price = soup.find_all("div", class_="yourprice")
    match = re.search("\d+\.\d\d", str(price))
    if match != None:
        print("  $%s" % match.group(0))
    else:
        print("  Error retrieving price.")

print(divider)

