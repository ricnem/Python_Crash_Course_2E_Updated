# create a variable to store the text file.
file = 'learning_python.txt'

# open the file as file_object then store it to the
# variable lines to read each line and make a list.
with open(file) as file_object:
    lines = file_object.readlines()

# use a for loop to loop through all the list inside the 'lines'
# strip whitespace in each line loop then print each line while replacing
# 'python' string to 'C'
for line in lines:
    line = line.rstrip()
    print(line.replace('python', 'C'))



