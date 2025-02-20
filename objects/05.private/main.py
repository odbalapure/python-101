import weakref

class MyClass:
    def __init__(self):
        # Name mangling is being applied here
        # This process changes the variable's name internally to prevent
        # accidental access or modification from outside the class
        # This is more of a convention rather than a strict enforcement of data privacy.
        self.__private_var = 10

    def show_private(self):
        print(self.__private_var)

obj = MyClass()

obj._MyClass__private_var = 20

# NOTE: Using obj._MyClass__private_var will fix the error
# Manging changes the name of the variable, hence it can't be accessed directly
# print(obj.__private_var)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Creating an instance of Person
person = Person("Alice", 30)

# Using repr() explicitly
print(repr(person))  # Output: Person(name='Alice', age=30)

# In the interpreter, you can just type the object and it will use __repr__ by default:
person  # Output: Person(name='Alice', age=30)


class TrainingData:
    pass

class Hyperparameter:
    """A hyperparameter value and the overall quality of the classification."""
    def __init__(self, k: int, training: TrainingData) -> None:
        self.k = k
        self.data: weakref.ReferenceType[TrainingData] = weakref.ref(training)
        self.quality: float

import weakref

class SomeClass:
    pass

obj = SomeClass()
weak_ref = weakref.ref(obj)

print(weak_ref())

del obj 
print(weak_ref())
