from lxml.etree import tostring
from lxml.html.soupparser import fromstring
from urllib.parse import urlsplit, parse_qsl
from SiteClient.Login import Login
from SiteClient.Exceptions import NoOrderError, OrderNotFoundError

class Orders(Login):
    """
    Orders

        Retrieves Orders information
    """


    def __init__(
        self,
        username: str,
        password: str
    ) -> None:
        """
        Tries to log in the user given the credentials.

        Args:
            - username ( str ): the username used to login on the site.
            - password ( str ): the password user to login on the site

        Returns:
            bool: Success of the login operation.

        Raises:
            LoginError: Raised when login fails.

        """

        super().__init__(username, password)


    def get_orders_list(
        self
    ) -> list:
        """
        Retrieves a list of placed orders

        Returns:
            list: List of orders in dict format

        Raises:
            NoOrderError: Raised when there is no order placed on the site.

        """

        response = self.session.get("http://automationpractice.com/index.php?controller=history")

        self.HTMLParser.set_html(response.text)

        tbody = self.HTMLParser.find_elements_by_xpath("//tbody/tr")

        if not len(tbody):
            raise NoOrderError()

        orders = list()

        for tr in tbody:

            tr = self.HTMLParser.convert_node(tr)
            tds = tr.xpath("//td")

            orders.append({
                "reference": self._find_reference(tds[0]),
                "date": tds[1].text_content().strip(),
                "value": tds[2].get("data-value"),
                "payment_method": tds[3].text_content(),
                "status": self._find_status(tds[4]),
                "invoice_link": self._find_invoice_link(tds[5]),
                "id_order": self._find_id(tds[5])
            })

        return orders


    def _find_reference(
        self,
        td
    ) -> str:

        td = self.HTMLParser.convert_node(td)

        [ a ] = td.xpath("//a")
        return a.text_content().strip()


    def _find_status(
        self,
        td
    ) -> str:

        td = self.HTMLParser.convert_node(td)

        [ span ] = td.xpath("//span")
        return span.text_content().strip()


    def _find_invoice_link(
        self,
        td
    ) -> str:

        td = self.HTMLParser.convert_node(td)

        [ a ] = td.xpath("//a")
        
        return a.get("href")


    def _find_id(
        self,
        td
    ) -> str:

        td = self.HTMLParser.convert_node(td)

        [ a ] = td.xpath("//a")
        url = parse_qsl( urlsplit( a.get("href") ).query )
        url = dict(url)

        return url["id_order"]




        