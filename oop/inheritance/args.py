from typing import Any

# Note: The **kwargs parameter basically collects any keyword arguments passed into the method
# that were not explicitly listed in the parameter list. These arguments are stored in a dictionary 
# named kwargs (we can call the variable whatever we like, but convention suggests kw or kwargs).
#  When we call a method, for example, super().__init__(), with **kwargs as an argument value, it 
# unpacks the dictionary and passes the results to the method as keyword arguments.
class ContactList(list["Contact"]):
  def search(self, name: str) -> list["Contact"]:
      matching_contacts: list["Contact"] = []
      for contact in self:
          if name in contact.name:
              matching_contacts.append(contact)
      return matching_contacts

class Contact:
  all_contacts = ContactList()

  def __init__(self, /, name, email, **kwargs) -> None:
    # super().__init__(**kwargs) can be beneficial for avoiding the need to type every possible argument, 
    # especially when you're dealing with classes that inherit from multiple classes or need to handle a 
    # large number of potential arguments.
    super().__init__(**kwargs) # type: ignore [call-arg] 
    self.name = name
    self.email = email
    self.all_contacts.append(self)

  def __repr__(self) -> str:
    return (f"{self.__class__.__name__}(" f"{self.name!r},{self.email!r}" f")")

class AddressHolder:
  def __init__(
    self,
    /,
    street: str = "",
    city: str = "",
    state: str = "",
    code: str = "",
    **kwargs
  ) -> None:
  
    super().__init__(**kwargs) # type: ignore [call-arg] 
    self.street = street
    self.city = city
    self.state = state
    self.code = code
        
class Friend(Contact, AddressHolder):
  def __init__(self, /, phone: str = "", **kwargs) -> None:
    super().__init__(**kwargs)
    self.phone = phone

print(Friend(name = "this", email = "that", street = "something"))
print(AddressHolder)
