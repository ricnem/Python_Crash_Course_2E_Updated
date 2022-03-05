prompt1 = "What is your first name?: "
prompt2 = "\nWhat is your last name?: "


filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(f"{input(prompt1).title()} {input(prompt2).title()}")



