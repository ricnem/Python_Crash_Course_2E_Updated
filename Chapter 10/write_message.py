filename = 'nem.txt'

with open(filename, 'w') as file_object:
    file_object.write("Learn from your setbacks!")

    x = 5
    while x > 0:
        file_object.write("\nParang awa mo na...")
        x -= 1

