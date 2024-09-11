# modules
# --------------------------------------------------

# functions
# --------------------------------------------------
import session_20
x = session_20.myfunc(10, 20)
print(x)


# Naming a Module
import modules.mymodule01 as x
x.greeting("Jonathan")



# Import From Module
from modules.mymodule01 import greeting
greeting("Jonathan")


from modules.mymodule01 import *
greeting("Jonathan")







# import data
# --------------------------------------------------
import session_20
x = session_20.person1['country']
print(x)






# Date and time
# --------------------------------------------------
import datetime
x = datetime.datetime.now()
print(x)



x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))





# Creating Date Objects
# --------------------------------------------------
import datetime
x = datetime.datetime(2024, 5, 17)
print(x)



# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# --------------------------------------------------
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%3"))

print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))








# Python Math Module
# --------------------------------------------------
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)


x = abs(-7.25)
print(x)


x = pow(4, 3)
print(x)






import math
x = math.sqrt(64)
print(x)






import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1



import math
x = math.pi
print(x)









# json
# --------------------------------------------------

# Parse JSON - Convert from JSON to Python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])





# Parse JSON - Convert from Python to JSON
# --------------------------------------------------
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)






# Convert from Python to JSON and vice versa
# --------------------------------------------------
# Python  =======>   JSON
# dict    =======>   Object
# list    =======>   Array
# tuple   =======>   Array
# str     =======>   String
# int     =======>   Number
# float   =======>   Number
# True    =======>   true
# False   =======>   false
# None    =======>   null

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))












# RegEx Module
# --------------------------------------------------

# findall()
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



# search() Function: The search() function searches the string for a match, and returns a Match object if there is a match.
# --------------------------------------------------
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)
print("The first white-space character is located in position:", x.start())











# split() Function: The split() function returns a list where the string has been split at each match:
# --------------------------------------------------
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



# maxsplit parameter:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)








# sub() Function: The sub() function replaces the matches with the text of your choice:
# --------------------------------------------------
import re
txt = "The rain in Spain"
x = re.sub("\s", "...", txt)
print(x)


# count parameter:
import re
txt = "The rain in Spain"
x = re.sub("\s", "...", txt, 2)
print(x)











# --------------------------------------------------
# PIP
# --------------------------------------------------

# check if pip installed
# pip --version


# install it form pip
# pip install camelcase
# pip uninstall camelcase
# pip list


# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))