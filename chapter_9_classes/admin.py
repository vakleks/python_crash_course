class User:
    """Create a new user."""

    def __init__(self, first_name, last_name):
        """Initiate new user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def create_user(self):
        """Add info about new user."""
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        """Greeting user."""
        print(f"Hi, {self.first_name}! \nThank you for registration, welcome)")


class Admin(User):
    """Class Admin extends class User."""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privilegies(self):
        """Show admin's privilegies."""
        print("Privilegies:")
        for privilegie in self.privileges:
            print(f"* {privilegie};")

admin_one = Admin('Anakin', 'Skyworker')
admin_one.privileges = ['can add post', 'can edit post', 'can delete post']
admin_two = Admin('Obi Van', 'Kenoby')
admin_two.privileges = ['can delete user', 'can edit admin`s privilegies']

admin_one.create_user()
admin_one.show_privilegies()
admin_two.create_user()
admin_two.show_privilegies()

