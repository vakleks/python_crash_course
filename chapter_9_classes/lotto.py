from random import choice

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
characters = ['a', 'b', 'c', 'd', 'e']

win_digit = choice(digits)
win_character = choice(characters)

print(f"The winner is {win_digit}-{win_character.title()}!")


