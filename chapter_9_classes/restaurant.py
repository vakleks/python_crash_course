class Restaurant:
    """Create a restaurant."""

    def __init__(self, name, cuisine):
        """Initiate name and cuisine."""
        self.name = name.title()
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Show info about the restaurant."""
        print(f"{self.name} is a restaurant of {self.cuisine} cuisine.")

mcdonalds = Restaurant('Mc.Donalds', 'american')
rukkola = Restaurant('Rukkola', 'italian')
sushiya = Restaurant('Sushiya', 'japanese')

mcdonalds.describe_restaurant()
rukkola.describe_restaurant()
sushiya.describe_restaurant()
