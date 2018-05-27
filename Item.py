class Item(object):
    """ Item to search for price """

    def __init__(self, a_name, a_url, an_html_element):
        # Name for the item
        self.name = a_name
        # URL
        self.url = a_url
        # HTML element that contains the item price
        # If a string containing only alphabets is specified, then self.html_element
        #   will be used in the find_all command
        # If "itemprop" is specified, then the following find_all will be used:
        #   soup.find_all("span", itemprop="price")
        # If "priceblock_ourprice" is specified, then the following find_all will be used:
        #   soup.find_all("span", id="priceblock_ourprice")
        self.html_element = an_html_element
        pass

