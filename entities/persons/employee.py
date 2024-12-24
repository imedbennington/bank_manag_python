from .person import Person

class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str, position: str):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position

    def __str__(self):
        return f"Employee: {self.name}, Age: {self.age}, ID: {self.employee_id}, Position: {self.position}"
