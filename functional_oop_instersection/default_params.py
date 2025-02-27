# ===================================
# DEFAUTL ARGUMENTS
# ===================================

# we can provide a default value for a parameter using an equals sign.
# If the calling code does not supply an argument value for the parameter, 
# it will be assigned the given default value
# If a value of None is used as the default for optional parameter values, 
# the typing module lets us describe this using the Optional type hint.

# Type of arguments
#
# Positional only: For methods with less no. of arguments
# Keyword only: After the *, the argument values must have a keyword supplied. This can be helpful to make rarely used options more visible. It can help to think of keywords as keys to a dictionary.

from typing import Optional, Any

def latitude_dms(deg: float, min: float, sec: float = 0.0, dir: Optional[str] = None) -> str:
  if dir is None:
    dir = "N"
  return f"{deg:02.0f}° {min+sec/60:05.3f}{dir}"

print(latitude_dms(36, 51, 2.9, "N"))
# Or use a keyword parameter to use a default value
print(latitude_dms(36, 51, 2.9, dir = "N"))

# "*" denotes that all arguments after it must be keyword-only arguments.
# Not using a * will result in an error i.e. Non-default argument follows default argument
def kw_only(
    x: Any, y: Any = 'y', str = "defaultkw", *, a: bool, b: str = "only"
) -> str:
  return f"x={x}, y={y}, a={a}, b={b}"

# x and y are positional arguments, while a and b are keyword arguments.
# Not providing a value for "a" will result in a TypeError error.
# *TypeError: kw_only() missing 1 required keyword-only argument: 'a'*
# NOTE: As long as "a" and "b" are passed, the order doesn't matter.
print(kw_only('x', b=True, a=False))

# ===================================
# MORE ON DEFAULTS
# ===================================

# number = 5
# def funky_function(x: int = number) -> str:
#     return f"{x = }, {number = }"

# print(funky_function(42)) # x = 42, number = 5
# number = 7
# print(funky_function()) # x = 5, number = 7

# Fix the above issue with an Optinal and default value
# NOTE: Such usage of global varaibles MUST be well documented
def better_function(x: Optional[int] = None) -> str:
  if x is None:
    x = number
  return f"better: {x = }, {number = }"

number = 3
result = better_function()
print(result)

from typing import List

# BAD DEFAULT
def bad_default(tag: str, history: list[str] = []) -> list[str]:
  """
  A Very Bad Design (VBDTM).
  It will create only one instance of the mutable object
  This object will be reused
  """
  history.append(tag)
  return history

result = bad_default("tag1")
print(result) # ['tag1']
result2 = bad_default("tag21")
print(result2) # ['tag1', 'tag21']

# GOOD DEFAULT
def good_default(
    tag: str, history: Optional[list[str]] = None
) -> list[str]:
    history = [] if history is None else history
    history.append(tag)
    return history

result = good_default("tag1")
print(result) # ['tag1']
result2 = good_default("tag21")
print(result2) # # ['tag21']

