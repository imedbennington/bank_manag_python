class Person:
    def __init__(self, firstname, lastname, email):
        self._firstname = firstname  # Use underscore for private variables
        self._lastname = lastname
        self._email = email

    # Getter for firstname
    @property
    def firstname(self):
        return self._firstname

    # Setter for firstname
    @firstname.setter
    def firstname(self, value):
        if not isinstance(value, str):
            raise ValueError("Firstname must be a string.")
        self._firstname = value

    # Getter for lastname
    @property
    def lastname(self):
        return self._lastname

    # Setter for lastname
    @lastname.setter
    def lastname(self, value):
        if not isinstance(value, str):
            raise ValueError("Lastname must be a string.")
        self._lastname = value

    # Getter for email
    @property
    def email(self):
        return self._email

    # Setter for email
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string.")
        self._email = value

    def __str__(self):
        return f"Firstname: {self.firstname}, Last name: {self.lastname}, Email: {self.email}"
