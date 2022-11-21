#brands list
brands = ['samsung', 'xiaomi', 'apple', 'nokia', 'oppo', 'huawei', 'meizu']
print("The first three items in this list are:")
print(brands[:3])

print("\nThree items from the middle of the list are:")
print(brands[2:5])

print("\nThe last three items in the list are:")
print(brands[-3:])

#pizza list
pizzas = ['peperoni', 'margarita', 'toscana']
friend_pizzas = pizzas[:]

pizzas.append('hawaian')
friend_pizzas.append('cheese')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for friends_pizza in friend_pizzas:
    print(friends_pizza.title())


