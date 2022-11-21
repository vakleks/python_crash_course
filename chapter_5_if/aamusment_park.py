age = 4

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost in $40.")

#better variant

age = 65

if age < 4:
    price = 0
elif age <18:
    price = 25
elif age < 60:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

#or another
age = 60

if age <4:
    price = 0
elif age < 18:
    price = 25
elif age <60:
    price = 40
elif age >= 60:
    price = 20

print(f"Yor admission cost is ${price}.")

