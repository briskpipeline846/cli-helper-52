class CLIHelperError(Exception):
    """Base exception class for cli-helper-52."""
    pass

class ValidationError(CLIHelperError):
    """Raised when input validation fails."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when config is missing or invalid."""
    pass

class OperationTimeoutError(CLIHelperError):
    """Raised when an operation exceeds time limit."""
    pass

class ResourceNotFoundError(CLIHelperError):
    """Raised when a requested resource is missing."""
    pass

def handle_cli_exception(e: Exception) -> None:
    """Utility to map internal exceptions to user messages."""
    if isinstance(e, ValidationError):
        print(f"[!] Validation failure: {e}")
    elif isinstance(e, ConfigurationError):
        print(f"[!] Config issue detected: {e}")
    elif isinstance(e, OperationTimeoutError):
        print(f"[!] Operation timed out: {e}")
    else:
        print(f"[!] Unexpected error occurred: {e}")