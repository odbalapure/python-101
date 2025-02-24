class Person:
    def __init__(self, name):
        self._name = name
        self.__name = name

    @property
    def get_name(self):
        return self.__name
    
    def get_single_underscore_name(self):
        return self._name

    def set_single_underscore_name(self, name):
        self._name = name

print(Person("Om").get_name)
print(Person("Hari").get_single_underscore_name())

# Bear in mind that, even with the name property, the code is not 100% safe. 
# People can still access the _name attribute directly and set it to an empty string 
# if they want to. But if they access a variable we’ve explicitly marked with an 
# underscore to suggest it is private, they’re the ones that have to deal with the 
# consequences, not us. We established a formal contract, and if they elect to break 
# the contract, they own the consequences.

# -----------------------------------------------------------------------

class MyClass:
    def __init__(self):
        self._value = 0

    def get_value(self):
        print(f"get_value called")
        return self._value

    def set_value(self, value):
        print(f"set_value called with {value}")
        if value < 0:
            raise ValueError("Value cannot be negative")
        self._value = value

    def delete_value(self):
        print(f"delete_value called")
        del self._value

    value = property(get_value, set_value, delete_value)

obj = MyClass()
print(obj.value) # get_value called
obj.value = 10 # set_value called with 10
del obj.value # delete_value called

# -----------------------------------------------------------------------

# Python also allows you to define property using a decorator for a cleaner syntax
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name

    @name.deleter
    def name(self):
        del self._name

om = Person("Om")
print(om.name) # Om

om.name = "Omi"
print(om.name) # Omi

# del om.name
# print(om.name) # AttributeError: 'Person' object has no attribute '_name'

# -----------------------------------------------------------------------
