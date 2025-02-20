# Modules in python are just files, nothing more.
# import database
# db = database.Database("data.db")

# Import only the required class using the "from...import" syntax
# from database import Database
# db = Database("data.db")

# Import everything from the database module
# from database import *

# NOTE: Its always better to import only the required classes or functions from a module
# We can quickly identify where the "Database" class comes from
# It avoids conflicting names, say we have two modules with the same class name "Database"
# It will also import classes or modules that were themselves imported in the module/file

# Type "import this" in the interactive interpreter to see the "Zen of Python" poem

class Database:
    def display(self) -> None:
        print("Displaying database contents")
