filenames = ['cats.txt', 'dogs.txt', 'sheeps.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"This file {filename} can not be found.")



