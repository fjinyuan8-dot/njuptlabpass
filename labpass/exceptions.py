"""Domain exceptions with safe, user-facing messages."""
from __future__ import annotations


class LabPassError(Exception):
    """Base class for expected application errors."""


class ConfigurationError(LabPassError):
    """Invalid local configuration or command-line input."""


class AuthenticationError(LabPassError):
    """Authentication could not be completed."""


class AuthenticationExpiredError(AuthenticationError):
    """The authenticated session is no longer valid."""


class NetworkError(LabPassError):
    """A network request failed before a reliable response was received."""


class ApiError(LabPassError):
    """The remote API rejected a request."""


class LockConflictError(ApiError):
    """The remote API could not acquire its mutation lock."""


class ResponseFormatError(ApiError):
    """The remote API returned an unexpected response shape."""


class SubmissionUncertainError(ApiError):
    """A POST timed out, so the remote mutation may or may not have happened."""
