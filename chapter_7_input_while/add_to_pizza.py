prompt = "\nPlease, add topping to your pizza: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"{topping.title()} added to your pizza!")