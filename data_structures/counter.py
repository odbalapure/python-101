from collections import Counter

def letter_freq(sentence: str) -> Counter:
    """
    Find the frequency of each letter in sentence or word
    :param sentence: str
    :return: Counter
    """
    return Counter(sentence)

print(letter_freq("Hello"))

# -----------------------------------------------------------------------

responses = [
  "vanilla",
  "chocolate",
  "vanilla", 
  "vanilla", 
  "caramel",
  "strawberry", 
  "vanilla" 
]

favorites = Counter(responses).most_common(1)
name, frequency = favorites[0]
print(name, frequency)

# Other methods from Counter class
# elements()
print([item for item in Counter(responses).elements()])
print([item for item in Counter(responses).keys()])
# clear()
print(Counter(responses).clear())

# -----------------------------------------------------------------------
