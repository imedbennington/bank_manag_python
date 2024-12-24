from .person import Person

class Customer(Person):
    def __init__(self, firstname: str, lastname: str, email: str, customer_id: str):
        super().__init__(firstname, lastname, email)  # Initialize attributes from Person
        self._customer_id = customer_id  # Use underscore for private variable

    # Getter for customer_id
    @property
    def customer_id(self):
        return self._customer_id

    # Setter for customer_id
    @customer_id.setter
    def customer_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer ID must be a string.")
        self._customer_id = value

    def __str__(self):
        return (f"Customer: {self.firstname} {self.lastname}, Email: {self.email}, "
                f"ID: {self.customer_id}")