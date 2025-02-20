# Use of relative imports
# Using a module at the same level
from .database import Database

class Product:
    def __init__(self, product):
        self.product = product

    def get_product(self) -> str:
        db = Database()
        return self.product
