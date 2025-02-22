# ***************************************************************************************
# Dictionaries are unordered collections of key-value pairs
# - get()          : Returns the value for the specified key. If the key doesn't exist, returns None or a default value if provided.
# - setdefault()   : Returns the value of a key if it exists. If the key does not exist, inserts the key with the default value provided.
# - keys()         : Returns a view object that displays all the keys in the dictionary.
# - values()       : Returns a view object that displays all the values in the dictionary.
# - items()        : Returns a view object that displays all the key-value pairs in the dictionary as tuples.
# - update()       : Updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs.
# - pop()          : Removes and returns the value associated with the specified key. Raises KeyError if the key does not exist.
# - popitem()      : Removes and returns an arbitrary key-value pair as a tuple. Raises KeyError if the dictionary is empty.
# - clear()        : Removes all key-value pairs from the dictionary, making it empty.
# - copy()         : Returns a shallow copy of the dictionary.
# - fromkeys()     : Creates a new dictionary from the given sequence of keys with the specified value (default is None).
# - setdefault()   : Returns the value of the specified key if it exists, otherwise inserts the key with the given default value.
# - merge()        : New in Python 3.9, combines two dictionaries (uses `|` operator).
# - __contains__() : Checks if a key is in the dictionary. This is used with `in` operator.
# - __delitem__()  : Deletes a key-value pair from the dictionary. Equivalent to using `del` keyword.
# - len()          : Returns the number of key-value pairs in the dictionary.
# - in             : Checks if a key exists in the dictionary. Returns True if present, False if not.
# ***************************************************************************************

# Ways to create a dictionary
stocks = dict(current = 1235.20, high = 1242.54, low = 1231.06) 

stocks = {
    "GOOG": (1235.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84), 
}

# -----------------------------------------------------------------------

# Ways to access values
print(stocks["GOOG"])
# print(stocks["APPL"]) # Throws KeyError Exception

print(stocks.get("APPL")) # Does not throw an exception
print(stocks.get("APPL", "Not Found")) # "Not Found" is a default value

# -----------------------------------------------------------------------

# Getting and setting values

# "setdefault" gets a value from the dictionary
# If the key does not exist, it will set the key to the default value
# i.e. "None" in this case
print(stocks.setdefault("APPL", None))
print(stocks)

# Creates a new key-value pair
stocks["NSTL"] = (123.45, 123.45, 123.45)
print(stocks)

# NOTE: List cannot be used as keys

# -----------------------------------------------------------------------

x = 2020
y = 2305843009213695971 
print(hash(x) == hash(y)) # True
print(x == y) # False

x = "Om"
y = "Om"
print(hash(x) == hash(y)) # True
print(x == y) # True
