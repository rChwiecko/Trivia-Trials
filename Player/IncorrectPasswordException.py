class IncorrectPasswordException(Exception):
    """Exception raised for incorrect passwords."""

    def __init__(self, message="Incorrect password"):
        self.message = message
        super().__init__(self.message)
