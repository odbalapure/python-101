from typing import Optional
from database import Database
from point import Point

# Declares a global variable for this module
# Optional indicates the value of "db" can be "None"
db: Optional[Database] = None

def initialize_database(connection: Optional[str] = None) -> None:
    """
    Initialize a database connection.
    :param connection: Connection string
    :return: Database object
    """
    global db
    db = Database(connection)

def get_database(connection: Optional[str] = None) -> Database:
    """
    Get a database connection.
    :param str: Optional string
    :return: Database object
    """
    global db
    if not db:
        db = Database(connection)
    return db

# Executing code at the module level can lead to unintended side effects
# when the module is imported elsewhere.
pgdb = get_database("postgres://admin:password@localhost:5432/test_db")

Point()
