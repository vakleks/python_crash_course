import json

fav_number = input("What is your favorite number? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(fav_number, f)
    print(f"Your favorite number is {fav_number}, I'll remember it!")
