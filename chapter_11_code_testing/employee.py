class Employee():
    """A class to create an employee."""

    def __init__(self, first_name,  last_name, year_salary):
        """Initialize the employee."""
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = year_salary

    def give_raise(self, default_raise=5000):
        """Raise salary to employee."""
        self.salary += default_raise
