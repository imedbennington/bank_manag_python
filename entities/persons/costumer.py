from .person import Person

class Customer(Person):
    def __init__(self, name: str, age: int, customer_id: str):
        super().__init__(name, age)
        self.customer_id = customer_id

    def __str__(self):
        return f"Customer: {self.name}, Age: {self.age}, ID: {self.customer_id}"
