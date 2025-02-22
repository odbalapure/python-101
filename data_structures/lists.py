# ***************************************************************************************
# The append(element) method adds an element to the end of the list.
# The insert(index, element) method inserts an item at a specific position.
# The count(element) method tells us how many times an element appears in the list.
# The index() method tells us the index of an item in the list, raising an exception if it can’t find it.
# The find() method does the same thing but returns -1 instead of raising an exception for missing items.
# The reverse() method does exactly what it says, it turns the list around.
# The sort() method sorts the list in ascending order.
# ***************************************************************************************

import string

# NOTE: This example tells us that list is not suitable for collecting different kinds of attribute values
# dict or a Counter would be much more efficient and readable
CHARACTERS = list(string.ascii_letters) + [" "]
def letter_frequency(sentence: str) -> list[tuple[str, int]]:
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        # index() can be slow
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    non_zero = [
        (letter, count)
        for letter, count in frequencies if count > 0
    ]
    return non_zero

txt = "A quick brown fox jumps over the lazy dog"
print(letter_frequency(txt))

# -----------------------------------------------------------------------

from typing import Optional, cast, Any
from dataclasses import dataclass
from datetime import datetime
from pprint import pprint

@dataclass(frozen=True)
class MultiItem:
    data_source: str
    timestamp: Optional[float]
    creation_date: Optional[str]
    name: str
    owner_etc: str

    def __lt__(self, other: Any) -> bool:
        if self.data_source == "Local":
            self_datetime = datetime.fromtimestamp(
                cast(float, self.timestamp)
            ) 
        else:
            self_datetime = datetime.fromisoformat(
                cast(str, self.creation_date)
            )
        if other.data_source == "Local":
            other_datetime = datetime.fromtimestamp(
                cast(float, other.timestamp)
            )
        else:
            other_datetime = datetime.fromisoformat(
                cast(str, other.creation_date)
            )
        return self_datetime < other_datetime
    
mi_0 = MultiItem("Local", 1607280522.68012, None, "Some File", "etc. 0")
mi_1 = MultiItem("Remote", None, "2020-12-06T13:47:52.849153", "Another File", "etc. 1")
mi_2 = MultiItem("Local", 1579373292.452993, None, "This File", "etc. 2")
mi_3 = MultiItem("Remote", None, "2020-01-18T13:48:12.452993", "That File", "etc. 3")
file_list = [mi_0, mi_1, mi_2, mi_3] 
file_list.sort()
pprint(file_list)

# -----------------------------------------------------------------------

from dataclasses import dataclass
from pprint import pprint
from typing import Any
from operator import methodcaller, attrgetter

@dataclass(frozen=True)
class Item:
    name: str
    price: float = 0.0
    quantity: int = 0
    
    def __lt__(self, other: Any) -> bool:
        return self.price < other.price

    @property
    def total(self) -> float:
        return self.price * self.quantity

    # If uncommented the ealier logic for __lt__ will be overriden        
    # def __lt__(self, other: Any) -> bool:
    #     return self.quantity > other.quantity

iphone = Item('iphone', 999.0, 2)
samsung = Item('samsung', 799.0, 10)
oppo = Item('oppo', 599.0, 1)
vivo = Item('vivo', 699.0, 3)

# print(iphone > samsung)
# phones = [iphone, samsung, oppo, vivo]
# phones.sort()
# pprint(phones)

# ***************************************************************************************
# NOTE: Instead of implementing the __lt__ method
# We can use the "key" argument in the sort method
# The "key" argument takes a function that returns a value to be used for sorting
# The "reverse" argument is used to sort in descending order if "reverse=True"
# ***************************************************************************************
phones = [iphone, samsung, oppo, vivo]

phones.sort(key=lambda phone: phone.price, reverse=False)
print(phones)

phones.sort(key=lambda phone: phone.name, reverse=True)
print(phones)

# Instead of using a lambda we could use "attrgetter" from the "operator" module
phones.sort(key=attrgetter("quantity"), reverse=False)
print(phones)

# Walrus operator (:=) in action
print([total := phone.total for phone in phones])

# -----------------------------------------------------------------------
