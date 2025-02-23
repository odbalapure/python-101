# class InvalidWithdrawal(Exception):
#     pass
# raise InvalidWithdrawal("You don't have enough balance")

from decimal import Decimal

class InvalidWithdrawal(Exception):
    def __init__(self, balance: Decimal, amount: Decimal) -> None:
        super().__init__(f"Account does not have {amount}")
        self.amount = amount
        self.balance = balance

    @property
    def overage(self) -> Decimal:
        return self.amount - self.balance

try:
    raise InvalidWithdrawal(Decimal("25.00"), Decimal("50.00"))
except InvalidWithdrawal as e:
    print(f"Sorry withdrawal amount is more than the balance by {e.overage}")

# Criterias for defining custom exceptions:
# - They mus clearly describe what went wrong.
# - Client progammer should know how to fix it, whether its a 
# bug in their code or they need to handle that exception.
# - The handling should be distinct from other exceptions.

# NOTE:Python programmers tend to follow a model summarized by “It’s Easier to Ask Forgiveness Than Permission,” 
# sometimes abbreviated EAFP. The point is to execute code and then deal with anything that goes wrong. 
# The alternative is described as “Look Before You Leap,” often abbreviated LBYL. This is generally less popular. 
# The try/except pattern often forces you to handle these operations atomically (in one uninterruptible step), 
# making race conditions less likely.
