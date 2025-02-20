import ecommerce.products
watch = ecommerce.products.Product("Samsung Galaxy Watch4")
print(watch.get_product())

from ecommerce.products import Product
iphone = Product("Apple iPhone 4s")
print(iphone.get_product())

# Imports coming from ecommerce/__init__.py
# Instead of contact package or Database module
from ecommerce import Database, Email
Database()
Email()
