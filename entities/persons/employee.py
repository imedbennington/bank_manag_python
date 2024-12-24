from .person import Person

class Employee(Person):
    def __init__(self, firstname: str, lastname: str, email: str, employee_id: str, position: str):
        super().__init__(firstname, lastname, email)  # Initialize attributes from Person
        self._employee_id = employee_id  # Use underscore for private variables
        self._position = position

    # Getter for employee_id
    @property
    def employee_id(self):
        return self._employee_id

    # Setter for employee_id
    @employee_id.setter
    def employee_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Employee ID must be a string.")
        self._employee_id = value

    # Getter for position
    @property
    def position(self):
        return self._position

    # Setter for position
    @position.setter
    def position(self, value):
        if not isinstance(value, str):
            raise ValueError("Position must be a string.")
        self._position = value

    def __str__(self):
        return (f"Employee: {self.firstname} {self.lastname}, Email: {self.email}, "
                f"ID: {self.employee_id}, Position: {self.position}")