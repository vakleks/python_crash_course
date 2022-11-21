def describe_animal(animal_type, pet_name):
    """Show info about domestic pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_animal('hamster', 'harry')
describe_animal('dog', 'willie')

#rewrite the same function with key-arguments

def about_animal(animal_type='hamster', pet_name='harry'):
    """Show info about domestic pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

about_animal()

