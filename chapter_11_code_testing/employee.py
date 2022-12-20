class Employee:
    """Modeling employee."""

    def __init__(self, name, year_salary):
        """Initiate attributes that describe the employee."""
        self.name = name
        self.year_salary = year_salary

    def give_raise(self):
        """Add $5k to year salary, or another value of raise."""
        self.year_salary += 5000
