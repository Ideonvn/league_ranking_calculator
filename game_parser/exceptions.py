class GameParseException(Exception):
    """Exception raised when there is an error parsing a game."""

    def __init__(self, raw_line):
        """
        Initialize a GameParseException.

        Parameters:
        - raw_line (str): The raw line that caused the parsing error.
        """
        self.message = f'Parse Failed, invalid input provided: {raw_line}'

    def __str__(self):
        """
        Return a string representation of the exception.

        Returns:
        - str: A string representation of the exception.
        """
        return self.message
