filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"File {filename} contents:")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("Such file is not exist!")