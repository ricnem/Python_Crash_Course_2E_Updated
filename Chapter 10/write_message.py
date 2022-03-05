filename = 'nem.txt'

# opening a file in write mode using 'w'
with open(filename, 'w') as file_object:
    file_object.write("Learn from your setbacks!\n")

    x = 5
    while x > 0:
        file_object.write("\nParang awa mo na...\n")
        x -= 1

# opening a file in append mode using 'a'
with open(filename, 'a') as file_object:
    file_object.write("\nTranscend your self!")

