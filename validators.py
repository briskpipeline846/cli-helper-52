import re
from typing import Optional

def validate_email(email: str) -> bool:
    """Validate the format of an email address string.

    Args:
        email: The email string to validate.

    Returns:
        True if valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_port(port: int) -> bool:
    """Validate if a given integer is a valid TCP/UDP port.

    Args:
        port: The port number to check.

    Returns:
        True if the port is within the range 1-65535.
    """
    return 1 <= port <= 65535

def sanitize_input(user_input: Optional[str]) -> str:
    """Remove leading/trailing whitespace and return empty string if None.

    Args:
        user_input: The raw input string.

    Returns:
        The cleaned string.
    """
    if user_input is None:
        return ""
    return user_input.strip()