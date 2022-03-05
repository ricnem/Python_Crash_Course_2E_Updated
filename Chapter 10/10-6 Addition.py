try:
    x = int(input("Give me an x value: "))


    y = int(input("Give me a y value: "))


except ValueError:
    print(f"Bitch ass hoe, You can't add an integer and a string!")
else:
    sum = x + y
    print(f"\nThe sum of x and y that you just entered is {sum}.")