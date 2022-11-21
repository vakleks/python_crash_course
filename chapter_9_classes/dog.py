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

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age}.")
your_dog.roll_over()

