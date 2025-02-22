from collections import defaultdict

def letter_freq(sentence: str) -> dict[str, int]:
    """
    Find the frequency of each letter in sentence or word
    :param sentence: str
    :return: dict[str, int]
    """
    frequencies: dict[str, int] = {}
    for letter in sentence:
        freq = frequencies.setdefault(letter, 0)
        frequencies[letter] = freq + 1
    return frequencies

def letter_freq_default_dict(sentence: str) -> defaultdict[str, int]:
    """
    Find the frequency of each letter in sentence or word
    :param sentence: str
    :return: defaultdict[str, int]
    """
    # NOTE: Default value for any key that doesn't exist yet will be the result of calling int()
    # It does not mean that every key is supposed to be of type integer
    frequencies: defaultdict[str, int] = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

print(letter_freq("kayak"))
print(letter_freq_default_dict("kayak"))

# -----------------------------------------------------------------------

# We can pass not just int() as a default value but also list(), set() or even a "dataclass"

from dataclasses import dataclass

@dataclass
class Price:
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

portfolio = defaultdict(Price)
portfolio["APPL"]

# This portfolio dictionary creates a default Prices object for unknown keys
# defaultdict(<class '__main__.Price'>, {'APPL': Price(current=0.0, high=0.0, low=0.0))
print(portfolio)

def make_defaultdict():
    return defaultdict(Price)

by_month = defaultdict(
    # lambda: make_defaultdict() # OR
    lambda: defaultdict(Price)
)

# {
#     "APPL": {
#         "Jan": Price(current=122.25, high=137.98, low=53.15),
#     }
# }
by_month["APPL"]["Jan"] = Price(current = 122.25, high = 137.98, low = 53.15)
print(by_month)

# -----------------------------------------------------------------------
