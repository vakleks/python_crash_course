class User:
    """Create a new user."""

    def __init__(self, first_name, last_name, age, sex):
        """Initiate new user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex

    def create_user(self):
        """Add info about new user."""
        print(f"{self.first_name} {self.last_name} is a {self.age} years old {self.sex}.")

    def greet_user(self):
        """Greeting user."""
        print(f"Hi, {self.first_name}! \nThank you for registration, welcome)")

john_dough = User('john', 'dough', 25, 'male')
sarrah_konnor = User('sarrah', 'konnor', 38, 'female')
jedi = User('obivan', 'kennobi', 30, 'male')

sarrah_konnor.create_user()
sarrah_konnor.greet_user()