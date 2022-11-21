availabli_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availabli_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have a {requested_topping}.")

print("\nFinished making your pizza!")