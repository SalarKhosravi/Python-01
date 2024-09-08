# Dictionaries
# --------------------------------------------------------------
# Dictionaries are used to store data values in key:value pairs.

di = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# As of Python version 3.7, dictionaries are ordered, changeable, and do not allow duplicates.
di = {
    "name": "Ali",
    "age": 32,
    "weight": 72.600,
    "married": True,
    "Kids": ["hassn", "sara", "Omid"],
    "age": 34
}


print(len(di))
print(type(di))

# The dict() Constructor
di = dict(name = "John", age = 36, country = "Norway")
di = {"name": "John", "age": 36, "country": "Norway"}
print(di)

# Access Dictionary
print(di["name"])
print(di.get("name"))



# keys, values, items
# --------------------------------------------------------------
di = {
    "name": "Ali",
    "age": 32,
    "weight": 72.600,
}
print(di.items())
print(di.keys())
print(di.values())



# Functions in 
# --------------------------------------------------------------
di = {
    "name": "Ali",
    "family": "Asadi",
}

di["age"] = 30
print(di)

di.update({"year": 2020})
di.update({"age": 40})
print(di)




# LOOP dict
# --------------------------------------------------------------

di = {
    "name": "Ali",
    "family": "Asadi",
    "age": 35
}

for x in di:
  print(x)

for x in di.keys():
  print(x)

for x in di.values():
  print(x)

for x, y in di.items():
  print(f"x: {x} , y: {y}")

for key, value in di.items():
  print(f"key: {key} , value: {value}")



# Comprehension
di = {
  "a": 3,
  "b": 6,
  "c": 8
}

newDi = { key: value for key, value in di.items() }
print(newDi)

newDi = { key: value * 2 for key, value in di.items() }
print(newDi)

