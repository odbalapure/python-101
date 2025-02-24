# When to choose attribute, property or a method
# NOTE: In Python, data, properties, and methods are all attributes of a class. 
# The fact that a method is callable does not distinguish it from other types of attributes.
# *attributes*: When no validation or simple mutation is needed.
# *properties*: When controlled access or validation is required with simple computation.
# *methods*: When complex logic, actions, or operations are required.

from urllib.request import urlopen
from typing import Optional
import time

class WebPage:
    def __init__(self, url: str) -> None:
        self.url = url
        self._content: Optional[bytes] = None
    
    @property
    def content(self) -> bytes:
        if self._content is None:
            print("Retreiving content from URL")
            with urlopen(self.url) as response:
                self._content = response.read()
        return self._content

webpage = WebPage("http://ccphillips.net/")

now = time.perf_counter()
content1 = webpage.content
first_fetch = time.perf_counter() - now

now = time.perf_counter()
content2 = webpage.content
second_fetch = time.perf_counter() - now

# assert content2 == content1, "Problem: Pages were different" # OR
print("Content was different..." if content1 != content2 else "Same content fetched!")

print(f"Initial Request     {first_fetch:.5f}")
print(f"Subsequent Requests {second_fetch:.5f}")

class AverageList(list[int]):
    @property
    def average(self) -> float:
        return sum(self) / len(self)

print(AverageList([1, 2, 3, 4, 5]).average) # 3.0
