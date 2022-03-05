import json

numbers = [5, 4, 7632, 25, 125, 622, 529, 565]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)