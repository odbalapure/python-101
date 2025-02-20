from contact import Contact

class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        # This is required to append the new contact
        # to the 'all_contacts' list[Contact] 
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self) -> str:
        """
        Overrided version of Contact's __repr__
        This is required due to the new 'phone' attribute
        """
        return f"Friend(name={self.name}, email={self.email}, phone={self.phone})"
    
om = Friend('Om', 'om.balapure@gmail.com', '+91-2312312012')
dusty = Friend("Dusty", "Dusty@private.com", "555-1212")
print(Contact.all_contacts)
