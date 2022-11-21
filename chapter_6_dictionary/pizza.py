#save information about the order
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheeese'],
}

#check the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
