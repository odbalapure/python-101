# Python has 2 ways to define similar things:
# - Duck typing
# - Inheritance
# NOTE: We can take inheritance a step further and use abstract
# class definition; they aren't directly usersable by themselves,
# but can be used through inheritance to create concrete classes.

# !!!NOTE!!!:
# "type" is the metaclass used to create classes, while 
# object is the base class of all classes.

from abc import ABC, abstractmethod

class MediaLoader(ABC):
    @abstractmethod
    def play(self) -> None:
        # Ellipsis tells that a useful body needs to be written 
        # in order to create a working, concrete subclass.
        ...

    @abstractmethod
    def ext(self) -> str:
        ...

# The attribute that lists all of the names that needs to be filled
# in to create a concrete class is "__abstractmethods__"
print(MediaLoader.__abstractmethods__) # frozenset({'ext', 'play'})

# NOTE:
# Instantiating a subclass w/o implementing the abstract method
# will result in a "TypeError"
class Wav(MediaLoader):
    # using a variable to satisfy concrete class implementation
    ext = '.ogg'

    def __init__(self):
        print("Created object succesfully")
    
    def play(self):
        pass

x = Wav()
