from bs4 import BeautifulSoup
import urllib2

divider = "====================================================================================="

print "Price check...\n"

if True:
    print divider
    print 'Merrell Moab Ventilator Wide'
    url = "http://www.merrell.com/US/en/moab-ventilator-wide-width/16220M.html"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    print "Sale: ", soup.find_all("span", class_="promo-price")
    print soup.find_all("span", itemprop="price")
    print

if True:
    print divider
    print 'Nebraska Furniture Mart Polk 12" sub'
    url = "https://www.nfm.com/DetailsPage.aspx?productid=31539166"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    print soup.find_all("div", class_="yourprice")
    print

print divider

