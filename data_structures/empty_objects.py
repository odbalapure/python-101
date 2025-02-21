o = object()
# AttributeError: 'object' object has no attribute 'x'
# It’s not possible to set any attributes on an object() that was instantiated directly.
# It takes a certain amount of system memory to keep track of each object’s attributes for 
# storing both the attribute name and its value. Even if no attributes are stored, memory 
# is allocated to make it possible to add attributes
o.x = 5

class MyClass:
  pass

om = MyClass()
om.name = 'Om Balapure'
print(om.name)
