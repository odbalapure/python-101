from dataclasses import dataclass
from pprint import pprint

# Implements the __init__ method
# Add default values to attributes
# (order=True) creates comparison special methods
# (fronzen=True) creates immutable objects

@dataclass(order=True)
class Stock:
    symbol: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

appl = Stock("APPL", 123.52, 53.15, 137.98)
print(appl)

goog = Stock("GOOG")
print(goog)

# -----------------------------------------------------------------------

from dataclasses import field

@dataclass(order=True, frozen=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

# Start comparing from the "name" attribute, if same it will move on to "current" attribute
stock_ordered1 = StockOrdered("GOOG", 1826.77, 1847.20, 1013.54) 
stock_ordered2 = StockOrdered("GOOG")
stock_ordered3 = StockOrdered("GOOG", 1728.28, high = 1733.18, low = 1666.33)
stock_ordered1 < stock_ordered2 
stock_ordered1 > stock_ordered2 
pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))

# frozen=True makes the objects immutable
# stock_ordered1.test = 'Test'

# -----------------------------------------------------------------------
