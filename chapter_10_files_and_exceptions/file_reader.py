filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears ion the first million digits of pi!")
else:
    print("You birthday does not appear in the first million digits of pi.")

#output first 50 symbols after dot
print(f"{pi_string[:52]}")
print(len(pi_string))

