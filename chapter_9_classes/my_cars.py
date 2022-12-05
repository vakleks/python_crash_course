import car

print("My cars:")

my_beetle = car.Car('volksvagen', 'Beetle', 2019)
print(f"* {my_beetle.get_descriptive_name()}")

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(f"* {my_tesla.get_descriptive_name()}")
