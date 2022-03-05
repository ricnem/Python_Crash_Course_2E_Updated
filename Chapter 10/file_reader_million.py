file_name = 'pi_one_million.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)

birthday = input("Enter your birthday in mmddyy form: ")

if birthday in pi_string:
    print("Your birthday is in the first million digits of pi!")
else:
    print("\nYour birthday is not in the first million digits of pi...")