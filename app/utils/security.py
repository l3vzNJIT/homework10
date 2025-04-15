from builtins import Exception, ValueError, bool, str
import secrets
from logging import getLogger
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHash

# Set up logging
logger = getLogger(__name__)

# Create a global Argon2 hasher instance
ph = PasswordHasher()  # You can customize time_cost, memory_cost, parallelism, etc.

def hash_password(password: str) -> str:
    """
    Hashes a password using Argon2.

    Args:
        password (str): The plain text password to hash.

    Returns:
        str: The hashed password.

    Raises:
        ValueError: If hashing the password fails.
    """
    try:
        return ph.hash(password)
    except Exception as e:
        logger.error("Failed to hash password: %s", e)
        raise ValueError("Failed to hash password") from e

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain text password against an Argon2 hash.

    Args:
        plain_password (str): The plain text password to verify.
        hashed_password (str): The Argon2 hashed password.

    Returns:
        bool: True if the password is correct, False otherwise.

    Raises:
        ValueError: If the hash format is incorrect or verification fails.
    """
    try:
        return ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False
    except InvalidHash:
        logger.error("Invalid hash format during password verification.")
        raise ValueError("Invalid hash format.")
    except Exception as e:
        logger.error("Error verifying password: %s", e)
        raise ValueError("Authentication process encountered an unexpected error") from e

def generate_verification_token():
    return secrets.token_urlsafe(16)
