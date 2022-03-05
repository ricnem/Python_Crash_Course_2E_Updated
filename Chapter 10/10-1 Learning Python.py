#reading contents of a file
with open('learning_python.txt') as file:
    contents = file.read()
print(contents.rstrip())


#reading line by line
filename = 'learning_python.txt'
print("----------------------------")
with open(filename) as object:
    for line in object:
        print(line.rstrip())
print("----------------------------")
#making a list of lines from a file.
with open(filename) as object:
    lists = object.readlines()

for line in lists:
    print(line.rstrip())