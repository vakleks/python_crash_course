import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        fav_number = json.load(f)
except FileNotFoundError:
    fav_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
        print(f"I'll remember your favorite number!")
else:
    print(f"Yor favorite number is {fav_number}!")
