class MyCustomError(Exception):
    """Base class for other custom exceptions"""
    pass
class endOfBoardException(MyCustomError):
    """Raised when a specific error code is needed."""
    def __init__(self, message):
        self.message = message
        super().__init__(f'Error: {message}')
