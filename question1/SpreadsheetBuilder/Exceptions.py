class SaveDirError(Exception):
    """Raised when the credentials given to login were wrong"""

    message = "The selected path doesn't exists"

    def __init__(
        self,
        *args
    ) -> None:
        super().__init__(self.message, *args)