import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse the JSON string into a Python dictionary
data = json.loads(json_string)

# Access the values in the dictionary
name = data['name']
age = data['age']
city = data['city']

print(name)  # Output: John
print(age)   # Output: 30
print(city)  # Output: New York
