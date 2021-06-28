class LoginError(Exception):
    """Raised when the credentials given to login were wrong"""

    message = "Login failed with given credentials"

    def __init__(
        self,
        *args
    ) -> None:
        super().__init__(self.message, *args)


class NoOrderError(Exception):
    """Raised when there is no order placed on the site"""

    message = "There is no placed Orders to retrieve"

    def __init__(
        self,
        *args
    ) -> None:
        super().__init__(self.message, *args)


class OrderNotFoundError(Exception):
    """Raised when there is no order placed on the site"""

    message = "No Orders found with given ID"

    def __init__(
        self,
        *args
    ) -> None:
        super().__init__(self.message, *args)