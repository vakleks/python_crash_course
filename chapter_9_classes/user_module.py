"""Set for creating users."""

class User():
    """Create a new user."""

    def __init__(self, first_name, last_name):
        """Initiate new user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def create_user(self):
        """Add info about new user."""
        print(f"{self.first_name} {self.last_name}.")

    def greet_user(self):
        """Greeting user."""
        print(f"Hi, {self.first_name}! \nThank you for registration, welcome)")