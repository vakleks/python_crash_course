filename = 'guests_book.txt'

print("Input your name.")
while True:
    name = input("\nWhat's your name?\n(input 'exit' when you finish.)")
    if name == 'exit':
        break
    else:
        with open(filename, 'a') as file:
            file.write(f"{name}\n")
        print(f"{name} add to guests book.")