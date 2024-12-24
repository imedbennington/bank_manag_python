from entities.persons.person import Person

class Account:
    def __init__(self, owner: Person, balance: float):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance:.2f}"
