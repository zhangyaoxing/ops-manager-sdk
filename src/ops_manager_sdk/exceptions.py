class OpsManagerError(Exception):
    """Base exception for SDK errors."""


class RequestError(OpsManagerError):
    """Raised when the HTTP request cannot be completed."""


class ApiError(OpsManagerError):
    """Raised when the server returns a non-success status code."""

    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(message)
        self.status_code = status_code


class AuthenticationError(ApiError):
    """Raised when authentication fails."""
