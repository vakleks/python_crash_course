print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nInput first number: ")
    if first_number == 'q':
        break
    second_number = input("\nInput second number: ")
    if second_number == 'q':
        break
answer = int(first_number) / int(second_number)
print(f"Result is: {answer}")

