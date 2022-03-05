while True:
    try:
        print("(Please type 'quit' and press enter when you're done.)\n")

        x = input("Give me an x value: ")
        if x == 'quit':
            break
        else:
            x = int(x)

        y = input("Give me a y value: ")
        if y == 'quit':
            break
        else:
            y = int(y)

    except ValueError:
        print(f"Bitch ass hoe, You can't add an integer and a string!\n")
    else:
        sum = x + y
        print(f"\nThe sum of x and y that you just entered is {sum}.\n")