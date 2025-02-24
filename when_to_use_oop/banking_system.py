from dataclasses import dataclass

class InvalidAmountError(Exception):
    ...

class InsufficientBalanceError(Exception):
    ...

@dataclass
class Account:
    _account_number: str
    _account_holder: str
    _balance: float = 0.0

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise InvalidAmountError("Balance cannot be negative")
        self._balance = balance
    
@dataclass
class Bank:
    account: Account = None

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Invalid deposit amount!")
            self.account.balance += amount
            print(f"Account credited by {amount}, current balance is {self.account.balance}")
        except InvalidAmountError as e:
            print(str(e))

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Invalid withdrawal amount!")
            if amount > self.account.balance:
                raise InsufficientBalanceError("Insufficient balance!")
            self.account.balance -= amount
            print(f"Account debited by {amount}, current balance is {self.account.balance}")
        except InvalidAmountError as e:
            print(str(e))
        except InsufficientBalanceError as e:
            print(str(e))

print("*" * 98)
print("\t\t\t\t\tBanking System")
print("*" * 98)

account = Account("118539001006040", "Jon Doe", 50000.0)
bank = Bank(account)

print(f"\nAccount number: {bank.account.account_number}")
print(f"Account holder: {bank.account.account_holder}\n")

print("Transactions:")
bank.deposit(100.0)
# Invalid amount
bank.deposit(-50.0)

bank.withdraw(300.0)
# Insufficient funds
bank.withdraw(100000.0)

print(f"\nYour current balance is: {bank.account.balance}")
