# ========================================================================
# Python built-in abstract classess
# ========================================================================

from __future__ import annotations
from collections.abc import Container

# Python Collections Class Hierarchy
#
# Abstract Base Classes:
# - Container: Defines __contains__(item) method
# - Iterable: Defines __iter__() method
# - Sized: Defines __len__(item) method
#
# Collection: Inherits from Container, Iterable, and Sized
#   Combines functionality of all three parent classes

# NOTE:
# All the *collections* that we use are the extensions of "Collection" abstract class
# "Collections" class is an extension of an even more fundamental abstraction "Container"
# This method is implemented by set, list, str, tuple, dict

print(Container.__abstractmethods__) # frozenset({'__contains__'})

class OddIntegers:
    def __contains__(self, x: int) -> bool:
        return x % 2 != 0

odd = OddIntegers()
# The result is True for both the cases due to Duck Typing
print(isinstance(odd, Container)) # True
print(issubclass(OddIntegers, Container)) # True

# "in" is used to check if a value exists in a container
# When you use "in" Python internally calls the __contains__() method
print(1 in odd) # True
print(2 in odd) # False

# ========================================================================
# Implementing the "Mapping" abstract class  
# ========================================================================

from collections import abc
from typing import Protocol, Any, overload, Union
from typing import Iterator, Iterable, Sequence
import bisect

class Comparable(Protocol):
    """
    Any class that implements all six comparison methods,
    will be considered compatible with the Comparable Protocol,
    without having to explicitly inherit from it.
    NOTE: Protocol classes are primarily for static type
    checking and have no runtime effect in Python.
    """
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

BaseMapping = abc.Mapping[Comparable, Any]

class Lookup(BaseMapping):
    @overload
    def __init__(self, source: Iterable[tuple[Comparable, Any]]) -> None:
        ...
    
    @overload
    def __init__(self, source: BaseMapping) -> None:
        ...

    def __init__(self, source: Union[Iterable[tuple[Comparable, Any]], BaseMapping, None] = None) -> None:
        sorted_pairs: Sequence[tuple[Comparable, Any]]
        if isinstance(source, Sequence):
            sorted_pairs = sorted(source)
        elif isinstance(source, abc.Mapping):
            sorted_pairs = sorted(source.items())
        else:
            sorted_pairs = []
        self.key_list = [p[0] for p in sorted_pairs]
        self.value_list = [p[1] for p in sorted_pairs]

    def __len__(self) -> int:
        return len(self.key_list)

    def __iter__(self) -> Iterator[Comparable]:
        return iter(self.key_list)

    def __contains__(self, key: object) -> bool:
        index = bisect.bisect_left(self.key_list, key)
        return key == self.key_list[index]

    def __getitem__(self, key: Comparable) -> Any:
        index = bisect.bisect_left(self.key_list, key)
        if key == self.key_list[index]:
            return self.value_list[index]
        raise KeyError(key)

x = Lookup([["z", "Zillah"],
    ["a", "Amy"],
    ["c", "Clara"],
    ["b", "Basil"]])
print(x["c"]) # Clara
