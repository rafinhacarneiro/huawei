# -*- coding: utf-8 -*-
from requests import Session
from SiteClient.HTMLParser import HTMLParser
from SiteClient.Exceptions import LoginError

class Login:
    """
    Login

        Connects to the AutomationTesting's practice.

    """


    HTMLParser = HTMLParser()
    

    def __init__(
        self,
        username: str,
        password: str
    ) -> bool:
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

        self.session = Session()

        response = self.session.post(
            "http://automationpractice.com/index.php?controller=authentication",
            data={
                "email": username,
                "passwd": password,
                "back": "my-account",
                "SubmitLogin": ""
            }
        )

        self.HTMLParser.set_html(response.text)

        errors = self.HTMLParser.find_elements_by_xpath("//p/parent::div[contains(@class, 'alert-danger')]")
        
        if len(errors):
            raise(LoginError(username, password))

        return True
