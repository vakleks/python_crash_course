class Restaurant:
    """Create a restaurant."""

    def __init__(self, name, cuisine, status):
        """Initiate name and cuisine."""
        self.name = name.title()
        self.cuisine = cuisine
        self.status = status

    def describe_restaurant(self):
        """Show info about the restaurant."""
        print(f"{self.name} is a restaurant of {self.cuisine} cuisine.")

    def chek_status(self):
        """Show tha the restaurant is open now."""
        print(f"The {self.name} is {self.status} now.")

mcdonalds = Restaurant('Mc.Donalds', 'american', 'open')
rukkola = Restaurant('Rukkola', 'italian', 'closed')
sushiya = Restaurant('Sushiya', 'japanese', 'open')

mcdonalds.describe_restaurant()
mcdonalds.chek_status()
rukkola.describe_restaurant()
rukkola.chek_status()
sushiya.describe_restaurant()
sushiya.chek_status()
