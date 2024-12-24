from .account import Account

class CheckingAccount(Account):
    def __init__(self, owner, balance: float, overdraft_limit: float):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"CheckingAccount - {super().__str__()}, Overdraft Limit: ${self.overdraft_limit:.2f}"
