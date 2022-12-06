from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

six_sides = Die()
results = []
for roll in range(10):
    result = six_sides.roll_die()
    results.append(result)
print("\nRoll results of six sides die:")
print(results)

ten_sides = Die(sides=10)
results = []
for roll in range(10):
    result = ten_sides.roll_die()
    results.append(result)
print("\nRoll results of ten sides die:")
print(results)

twenty_sides = Die(sides=20)
results = []
for roll in range(10):
    result = twenty_sides.roll_die()
    results.append(result)
print("\nRoll results of twenty sides die:")
print(results)



