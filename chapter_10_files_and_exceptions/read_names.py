filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print(f"File {filename} contents:")
        print(contents)