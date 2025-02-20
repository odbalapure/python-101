from pprint import pprint

class ContactList(list["Contact"]):
    def search(self, name: str) -> list["Contact"]:
        matching_contacts: list[Contact] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    # all_contacts = []
    all_contacts = ContactList()

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    
    def __repr__(self) -> str:
        return f"Contact(name={self.name}, email={self.email})"

class Order:
    pass

class Supplier(Contact):
   def order(self, order: Order) -> None:
        print(
           "If this were a real system we would send "
           f"'{order}' order to '{self.name}'"
        )

# Creating objects of the "Contact"
# om = Contact('Om', 'om@gmail.com')
# shivam = Contact('Shivam', 'shivam@yahoo.com')

# Extending the "Contact" class
# iphone = Supplier('Test', '123')
# Contact(name=Test, email=123)
# Calls the __repr__() method on "Contact"
# pprint(iphone)

# Accessing all_contacts
# [Contact(name=Om, email=om@gmail.com),
#  Contact(name=Shivam, email=shivam@yahoo.com),
#  Contact(name=Test, email=123)]
# pprint(Contact.all_contacts)

# Extending the "list" class with a custom search method
# for c in Contact.all_contacts.search('Om'):
#     pprint(c)

jon1 = Contact('Jon Doe', 'jon@gmail.com')
jon2 = Contact('Jon Snow', 'jon@gmail.com')
jane = Contact('Jane Snow', 'jane@gmail.com')
[pprint(c) for c in Contact.all_contacts.search('Jon')]
