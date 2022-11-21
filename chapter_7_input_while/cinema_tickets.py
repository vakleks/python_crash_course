age = input("How old are you?: ")
age = int(age)

if age < 3:
    print("Ticket price for you is free!")
elif age < 12:
    print("Ticket price for you is $12!")
else:
    print("Ticket price for you is $15!")