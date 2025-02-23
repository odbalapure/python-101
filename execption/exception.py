from typing import (
    List,
    NoReturn
)

class EvenOnly(List[int]):
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Only integers can be added")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added")
        super().append(value)

even_list = EvenOnly()
even_list.append(2)
# even_list.append(3) # ValueError: Only even numbers can be added
print(even_list)

# Use None when your function might return None (either explicitly or implicitly) 
# but is not meant to raise an exception or loop forever.
# Use NoReturn when your function is designed to never return a value, 
# typically because it raises an exception or never exits (e.g., it enters an infinite loop).
def never_returns() -> NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

def handler() -> None:
    try:
        never_returns()
        print("Never executed")
    except Exception as e:
        print(f"Caught an exception: {e!r}")
    print("Exception handled")

handler()
