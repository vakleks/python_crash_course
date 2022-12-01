class Restaurant:
    """Create a restaurant."""

    def __init__(self, name, cuisine):
        """Initiate name and cuisine."""
        self.name = name.title()
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Show info about the restaurant."""
        print(f"{self.name} is a restaurant of {self.cuisine} cuisine.")


class IceCreamStand(Restaurant):
    """Create an icecream stand."""

    def __init__(self, name, cuisine='icecream'):
        super().__init__(name, cuisine)
        self.flavors = []

    def available_flavors(self):
        """Show available icecream flavors."""
        print("Available flawors:")
        for flavor in self.flavors:
            print(f"* {flavor.title()};")


my_icecream_stand = IceCreamStand('Sweet Frost')
my_icecream_stand.flavors = ['strawberry', 'raspberry', 'cherry', 'apple']

my_icecream_stand.describe_restaurant()
my_icecream_stand.available_flavors()


