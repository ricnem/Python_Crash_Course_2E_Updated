import json

username = input("Enter your name: ")

filename = 'username.json'
with open(filename, 'a') as f:
    json.dump(username.title(), f)
    print(f"We will remember you when you come back, {username.title()}!")