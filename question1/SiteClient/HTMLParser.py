from lxml.etree import tostring
from lxml.html.soupparser import fromstring

class HTMLParser:
    """
    Parser

        Parses HTML to plaintext

    """


    def set_html(
        self,
        html: str
    ) -> None:
        """
        Saves the HTML to futher search

        Args:
            - html ( str ): HTML string

        Returns:
            None

        """
        
        self.tree = fromstring(html)

    
    def find_elements_by_xpath(
        self,
        xpath: str
    ) -> list:
        """
        Searches for element by XPATH

        Args:
            - xpath ( str ): XPATH string.

        Returns:
            list: List of nodes that match the XPATH

        """
        
        return self.tree.xpath(xpath)

    
    def convert_node(
        self,
        el
    ):
        """
            Returns a new with elements only inside the node

            Returns
                A new node tree
        """
        return fromstring( tostring(el, pretty_print=True) )

        