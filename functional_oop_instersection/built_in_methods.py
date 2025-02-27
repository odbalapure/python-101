# ===================================
# len()
# ===================================

# There are numerous functions in Python that perform a task or calculate a result
# on certain types of objects without being methods on the underlying class. 
# They usually abstract common calculations that apply to multiple types of classes. 
# This is duck typing at its best; these functions accept objects that have certain attributes
# or methods, and are able to perform generic operations using those methods.

st = {1, 2, 3}
print(len(st)) # 3

lst = [1, 3, 4, 5]
print(len(lst)) # 4

# Why are we calling len() instead of calling __len__ on those objects?
# The main reason is efficiency
# 1. When we call the __len__() method of an object, the object has to look the method up in its namespace, 
# and, if the special __getattribute__() method (which is called every time an attribute or method on an object is accessed)
# is defined on that object, it has to be called as well. Furthermore, the __getattribute__() method may have 
# been written to do something clever, for example, refusing to give us access to special methods such as __len__(). 
# The len() function doesn’t encounter any of this. It actually calls the __len__() method on the underlying class,
# so len(myobj) maps to MyObj.__len__(myobj).
# 2. Another reason is maintainability. In the future, Python developers may want to change len() so that it can calculate 
# the length of objects that don’t have __len__()

# ===================================
# reversed()
# ===================================

# Takes any sequence as input and returns a copy of that sequence in reverse order
# reversed() calls the __reversed__() method on the class for the parameter
# If that method does not exist, reversed builds the reversed sequence itself using calls to __len__() and __getitem__()

print(list(reversed(lst))) # [5, 4, 3, 1]


# ===================================
# enumerate()
# ===================================

# It creates a sequence of tuples where 1st element in each tuple is an index and 2nd one is the original value
from pathlib import Path

with Path("data.md").open() as source:
    for index, line in enumerate(source, start=1):
        # 3d: no. will be padded with spaces on the left
        # rstrip: removes any trailing whitespaces
        print(f"{index:3d}: {line.rstrip()}")

#   1: Python 101
#   2: Abstract Classes
#   3: Functional & OOP overlap
#   4: Exceptions
#   5: Data structures

# abs(), str(), repr(), pow(), and divmod() map directly to the special 
# methods __abs__(), __str__(), __repr__(), __pow__(), and __divmod__().
# bytes(), format(), hash(), and bool() also map directly to the special 
# methods __bytes__(), __format__(), __hash__(), and __bool__().
