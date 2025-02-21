# Tuples are immutable
# If we wish to mutate a tuple; means we are using the wrong data structure
# They can be used as keys for dict or a member of set
# Useful while creating a (x,y) coordinates or (r,g,b) color

import datetime

def middle(stock, date):
    _, _, high, low = stock
    return (((high + low)/2), date)

print(middle(("APPL", 123.52, 53.15, 137.98), datetime.date(2024, 12, 4)))

# This will create a tuple
a = 100,
# <class 'tuple'>
print(type(a))

# Accessing values in a tuple
s = "AAPL", 132.76, 134.80, 130.53
print(s[2]) # 138.4
print(s[1:3]) # (132.76, 134.8)

# -----------------------------------------------------------------------

# "typing.NamedTuple" is used to clarify the contents of tuples

from typing import NamedTuple

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        """
        Decorator is used to define a method that acts like an attribute.
        It's a way to create read-only computed attributes.
        """
        return (self.high + self.low / 2)

# This new class will have "__init__(), __repr__(), __hash__(), and __eq__()"
# NOTE: Values can be passed in as positional or keyword arguments
appl1 = Stock("APPL", 123.52, 53.15, 137.98)
appl2 = Stock("AAPL", low = 137.98, current = 123.52, high = 53.15)

print(appl1.middle, appl2.middle) # 122.13999999999999 122.13999999999999

# -----------------------------------------------------------------------
