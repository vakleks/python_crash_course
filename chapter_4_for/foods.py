my_foods = ['pizza', 'falafel', 'carrot cake']

#make an aaray copy with slice
friend_foods = my_foods[:]

#add new dishes to our lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())
