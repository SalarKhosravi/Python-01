# Importing the json module
print('---------------------------------------------------')
import json


# Converting a Python dictionary to a JSON string (serialization)
print('---------------------------------------------------')
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "languages": ["English", "Spanish"]
}

json_string = json.dumps(data)  # Converts Python object to a JSON-formatted string
print("JSON string dumps:", json_string)





# Formatting JSON with indentation for readability
print('---------------------------------------------------')
json_pretty = json.dumps(data, indent=4)  # Adds indentation to make JSON more readable
print("Pretty JSON string:\n", json_pretty)




# Writing JSON data to a file
print('---------------------------------------------------')
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # Writes JSON data to a file with formatting



# Converting a JSON string back to a Python dictionary (deserialization)
print('---------------------------------------------------')
json_data = '{"name": "Bob", "age": 25, "city": "Chicago"}'
python_data = json.loads(json_data)  # Converts JSON-formatted string to Python object
print("Python dictionary:", python_data)




# Reading JSON data from a file
print('---------------------------------------------------')
with open("data.json", "r") as file:
    file_data = json.load(file)  # Reads JSON data from a file and converts it to a Python object
    print("Data from file:", file_data)
