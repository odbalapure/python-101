# We have to distinguish between two varieties of overloading here:
# - Overloading parameters to allow alternative types using Union[...] hints.
# - Overloading the method by using more complex patterns of parameters.

from typing import (
   Union,
   Any
)

# We could either use Union eg: Union[str, int] for an overloaded function
def add(x: Union[str, int], y: Union[str, int]): 
  return x + y

print(add(1, 2))
print(add("1", "2"))

# that accepts both a string and integer. And "Any" incase of more complext inputs.
def mandatory_params(x: Any, y: Any, z: Any) -> str: 
    return f"{x = }, {y = }, {z = }"

print(mandatory_params(1, 2, 3))
