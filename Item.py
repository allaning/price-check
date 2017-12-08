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
        self.html_element = an_html_element
        pass

    def get_name(self):
        """ Returns the name of the item """
        return str(self.name)

