print("Give me two numbers, and I'll add them.")
print("Enter 'exit' to quit.")

while True:
    first_number = input("\nInput first number: ")
    if first_number == 'exit':
        break
    second_number = input("\nInput second number: ")
    if second_number == 'exit':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add text to the number!")
    else:
        print(f"The sum is: {answer}")
