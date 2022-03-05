import json

filename = 'fav_number.json'

fav_number = input("Enter your favorite number: ")

with open(filename, 'w') as f:
    json.dump(fav_number, f)
    print(f"We'll remember your favorite number!")