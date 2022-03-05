filename = 'guest_book.txt'

prompt1 = "(Please type 'quit' and press enter when you are done.)"
prompt1 += "\nEnter your first name: "
prompt2 = "\nEnter your last name: "

with open(filename, 'w') as f:

    while True:

        first_name = input(prompt1)

        if first_name == 'quit':
            print("Thank you.")
            break
        else:
            print(f"{first_name.title()} entered the party! the entry has been recorded in the guest book.")
            f.write(f"{first_name.title()}\n")
            continue

