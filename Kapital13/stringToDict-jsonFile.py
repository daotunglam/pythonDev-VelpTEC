import json

# Read the JSON data from a file
with open('data.json') as json_file:
    data = json.load(json_file)

# Access the values in the dictionary
name = data['name']
age = data['age']
city = data['city']

print(name)
print(age)
print(city)
