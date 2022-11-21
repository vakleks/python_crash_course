class Dog:
    """Create a dog."""

    def __init__(self, name, age):
        """Initiate atributes name and age."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate command 'sit'."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate command 'roll over'."""
        print(f"{self.name} rolled over!")
