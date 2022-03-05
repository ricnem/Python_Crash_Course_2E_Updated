import json

filename = 'username.json'

def greet_user():

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input(f"What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")


greet_user()