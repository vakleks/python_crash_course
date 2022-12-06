from random import choice

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
characters = ['a', 'b', 'c', 'd', 'e']

first_number = choice(digits)
first_character = choice(characters)
second_number = choice(digits)
second_character = choice(characters)

win_combination = f"{first_number}{first_character.title()}{second_number}{second_character.title()}"

print(f"The winner is {win_combination}!")


