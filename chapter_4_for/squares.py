#output squares of numbers from 1 to 10
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

#same code less strings
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

#generator list - the same as a previous but in one raw
squares = [value**2 for value in range(1,11)]
print(squares)