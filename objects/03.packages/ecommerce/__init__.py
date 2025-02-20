from .database import Database
from .contact.email import Email

# The __all__ attribute in Python is not a method
# but rather a special variable that you define in a module or package
# Yes, that's correct! Anything not included in the __all__ list
__all__ = [Database, Email]
