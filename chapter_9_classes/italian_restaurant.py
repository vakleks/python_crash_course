import restaurant_module

my_restaurant = restaurant_module.Restaurant('Rukkola', 'italian', 'open')
my_restaurant.describe_restaurant()
my_restaurant.chek_status()

my_restaurant.number_served = 10
print(str(my_restaurant.number_served) + " numbers served.")

my_restaurant.increment_numbers_served(4)
print(str(my_restaurant.number_served) + " numbers served after update data.")