from typing import Protocol
from contact import Contact

# Protocol can have attributes with type hints, but not full assignment statements.
class Emailable(Protocol):
  email: str

class MailSender(Emailable):
  def send_mail(self, message: str) -> None:
    print(f"Sending mail to {self.email} with message '{message}'")
    # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass

e = EmailableContact("John B", "johnb@sloop.net")
print(Contact.all_contacts)
e.send_mail("Hello, test e-mail here")
