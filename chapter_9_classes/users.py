class User:
    """Create a new user."""

    def __init__(self, first_name, last_name, age, sex):
        """Initiate new user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def create_user(self):
        """Add info about new user."""
        print(f"{self.first_name} {self.last_name} is a {self.age} years old {self.sex}.")

    def greet_user(self):
        """Greeting user."""
        print(f"Hi, {self.first_name}! \nThank you for registration, welcome)")

    def increment_login_attempts(self):
        """Increment the numbers of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts."""
        self.login_attempts = 0

sarrah_konnor = User('sarrah', 'konnor', 38, 'female')
sarrah_konnor.create_user()
sarrah_konnor.greet_user()
sarrah_konnor.increment_login_attempts()
sarrah_konnor.increment_login_attempts()
sarrah_konnor.increment_login_attempts()
print(sarrah_konnor.login_attempts)
sarrah_konnor.reset_login_attempts()
print(sarrah_konnor.login_attempts)

