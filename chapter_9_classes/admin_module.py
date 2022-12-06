"""Module fo creating admins."""
from user_module import User

class Admin(User):
    """Class Admin extends class User."""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilegies = Privilegies()


class Privilegies():
    """Create Privilegies for Admin class."""
    def __init__(self, privilegies=[]):
        self.privilegies = privilegies

    def show_privilegies(self):
        """Show admin's privilegies."""
        print("Privilegies:")
        for privilegie in self.privilegies:
            print(f"* {privilegie};")
