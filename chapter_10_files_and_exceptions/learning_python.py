# open and read the full file
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

# open file fith for cycle in a file object
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# open file in list without with block
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

python_opportunities = ''
for line in lines:
    python_opportunities += line.rstrip()

print(python_opportunities)


