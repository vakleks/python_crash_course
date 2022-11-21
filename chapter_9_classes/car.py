class Car:
    """Modeling the car."""

    def __init__(self, make, model, year):
        """Initiate attributes that describe the car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return formatted meaningful name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

