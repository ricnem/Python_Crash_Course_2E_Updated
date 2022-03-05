try:
    print(5/0)
except ZeroDivisionError:
    print("\nYou can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    try:
        first_number = input("\nFirst Number: ")
        if first_number == 'q':
            break
        second_number = input("Second Number: ")
        if second_number == 'q':
            break
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("\nStop doing that!")