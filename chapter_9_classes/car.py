"""A set of classes for modeling gasoline and electric cars."""

class Car:
    """Modeling the car."""

    def __init__(self, make, model, year):
        """Initiate attributes that describe the car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return formatted meaningful name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Output message with car mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Inputodometer's data."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add data to odometer value."""
        self.odometer_reading += miles

class Battery():
    """Create a battery for ElectricCar class."""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Output message about battery value."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        """Charge battery to 100% capacity."""
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"Battery charged to {self.battery_size}-kWh.")

    def get_range(self):
        """Display a message about the distance that the car can drive according to the battery capacity"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Model electric car."""

    def __init__(self, make, model, year):
        """Add atributes of parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electrocar has no gas tank!"""
        print("This car doesn't need a gas tank!")




