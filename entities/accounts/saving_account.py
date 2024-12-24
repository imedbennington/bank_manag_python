from .account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance: float, interest_rate: float):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"SavingsAccount - {super().__str__()}, Interest Rate: {self.interest_rate}%"
