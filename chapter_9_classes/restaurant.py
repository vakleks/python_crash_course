class Restaurant:
    """Create a restaurant."""

    def __init__(self, name, cuisine, status):
        """Initiate name and cuisine."""
        self.name = name.title()
        self.cuisine = cuisine
        self.status = status
        self.number_served = 0

    def describe_restaurant(self):
        """Show info about the restaurant."""
        print(f"{self.name} is a restaurant of {self.cuisine} cuisine.")

    def chek_status(self):
        """Show tha the restaurant is open now."""
        print(f"The {self.name} is {self.status} now.")

    def set_numbers_served(self, number_served):
        """Show numver served."""
        self.number_served = number_served
        print(f"{number_served} numbers served." )

    def increment_numbers_served(self, add_number):
        """Add served numbers."""
        self.number_served += add_number


american_restaurant = Restaurant('Mc.Donalds', 'american', 'open')
italian_restaurant = Restaurant('Rukkola', 'italian', 'closed')
japanese_restaurant = Restaurant('Sushiya', 'japanese', 'open')

american_restaurant.describe_restaurant()
american_restaurant.chek_status()
american_restaurant.set_numbers_served(6)

