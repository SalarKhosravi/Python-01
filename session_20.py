# Functions
#-----------------------------------------------------------
# def functionaName(input):
#   codes body
# call the function

#-----------------------------------------------------------

def myfunc(x, y):
  return x + y

z = myfunc(2,3)
print(z)        # 5




# Sample function: a function that greet based on gender and age
#-----------------------------------------------------------
def say_hello(name, gender, age):
  if gender == 'male':
    if age > 18:
      print(f"Hello sir {name}")
    elif age > 9:
      print(f"Hi {name}")
    else:
      print(f"Hi {name}, my little boy")
  else:
    if age > 18:
      print(f"Hello madam {name}")
    elif age > 9:
      print(f"Hi {name}")
    else:
      print(f"Hi {name}, my cute girl")


say_hello('Sara', 'female', 5)
say_hello('Emilly', 'female', 15)
say_hello('Anne', 'female', 43)

say_hello('Nick', 'male', 6)
say_hello('Jack', 'male', 16)
say_hello('Adam', 'male', 28)

say_hello(name = 'Adam', age = 28, gender = 'male')
say_hello(age = 28, name = 'Adam', gender = 'male')





# Simple FUnction to calculate the sum of numbers in a list
#-----------------------------------------------------------
def sum_list_values(li):
  total = 0
  for i in li:
    total += i
    
  return total

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = sum_list_values(li)
print(sum)





# write a function like range()
# Step 1: Basic Code
#-----------------------------------------------------------
def myrange(start, end, step):
  i = start
  mylist = []
  while i < end: 
    if i % step == 0:
      mylist.append(i)
    i += 1
  return mylist


x = myrange(0, 10, 1)
print(x)
# x = myrange(end=10)




# Step 2: Medium Code
#-----------------------------------------------------------
def myRange2(start = 0, end = None, step = 1):
  # validation quantity
  if end == None:
    return 'invalid input'

  # validation type
  if type(start) != int or type(end) != int or type(step) != int:
    return 'input must be integer'

  i = start
  mylist = []
  while i < end: 
    if i % step == 0:
      mylist.append(i)
    i += 1
  return mylist



x = myRange2(3, 10, 2)
print(x)    

x = myRange2(0, 10, "a")
print(x)

x = myRange2(0, 10, None)
print(x)

x = myRange2(0, 10, None)
x = myRange2(start=10, end= 20)
x = myRange2()




# Step 3: Good Code
#-----------------------------------------------------------
def myRange3(start=None, end=None, step=None):
    # Handle cases where only one argument is provided (like range(stop))
    if end is None:
        if start is None:
            raise ValueError("At least one argument must be provided")
        end = start
        start = 0

    # Default step to 1 if not provided
    if step is None:
        step = 1

    # Check if start, end, and step are integers
    if not all(isinstance(arg, int) for arg in [start, end, step]):
        return 'input must be integer'
    
    # Check if step is zero
    if step == 0:
        raise ValueError("step argument must not be zero")

    mylist = []
    i = start
    
    # Generate the range
    if step > 0:
        while i < end:
            mylist.append(i)
            i += step
    else:
        while i > end:
            mylist.append(i)
            i += step

    return mylist

print(myRange3(0, 10, 1))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange3(0, 11, 2))   # [0, 2, 4, 6, 8, 10]
print(myRange3(3, 10, 2))   # [3, 5, 7, 9]
print(myRange3(0, 10, "a")) # input must be integer
print(myRange3(0, 10, None)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange3(None, 10, None)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange3(10, 0, -2))   # [10, 8, 6, 4, 2]

x = myRange3(10)
print(x)





# Step 4: Really advanced
#-----------------------------------------------------------
# Function for real Range() function to accpt input in this format (start:end:step)
def my_real_range(inputText):
    # Split the input string by ':'
    parts = inputText.split(':')

    # Initialize default values
    start = 0
    end = None
    step = 1
    
    # Convert parts to integers and handle missing values
    if len(parts) == 3:
        start = int(parts[0]) if parts[0] else 0
        end = int(parts[1]) if parts[1] else None
        step = int(parts[2]) if parts[2] else 1
    elif len(parts) == 2:
        start = int(parts[0]) if parts[0] else 0
        end = int(parts[1])
        step = 1
    elif len(parts) == 1:
        start = 0
        end = int(parts[0])
        step = 1
    else:
        return 'invalid input'
    
    # Default values for start, step, and end
    if end is None:
        raise ValueError("End cannot be unknown")
    
    if step is None:
        step = 1
    if start is None:
        start = 0
    
    if step == 0:
        raise ValueError("step argument must not be zero")

    # Generate the range list
    mylist = []
    i = start
    
    if step > 0:
        while i < end:
            mylist.append(i)
            i += step
    else:
        while i > end:
            mylist.append(i)
            i += step

    return mylist


# Test cases
print(my_real_range("0:10:1"))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_real_range("0:11:2"))   # [0, 2, 4, 6, 8, 10]
print(my_real_range("3:10:2"))   # [3, 5, 7, 9]
print(my_real_range("10:0:-2"))  # [10, 8, 6, 4, 2]
print(my_real_range("0:10"))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_real_range(":10:"))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_real_range(":20:2"))     # [5, 7, 9]













# unlimited inputs with *args for list alike
#-----------------------------------------------------------
def my_sum(*args):
  # print(args) # give me a tuple
  total = 0
  for i in args:
    total += i

  print(total)


my_sum(3)
my_sum(3, 2)
my_sum(3, 2, 4)
my_sum(3, 2, 4, 4, 5, 6, 8, 1, 2, 24, 13, 8 , 9, 10, 11, 200)


def my_func(x, *args):
  print(args)

my_func(1, 2, 3, 4)







# unlimited inputs with **kwargs for list alike
#-----------------------------------------------------------
def my_print(**kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(f"key: {key}, value: {value}")

my_print(name = "Ali", Family = "Kho", Age = 25, married = True)










# Order of inputs for functions
#-----------------------------------------------------------
# order is like this:
  # parameters
  # *args
  # default
  # **kwargs


def my_func(x, y, *args, z = 'ddd', **kwargs):
  return (x, y, args, z, kwargs)


print(my_func(2, 3, 4, 5, 6, name = 'Ali', age = 25))
print(my_func(2, 3, 4, 5, 6, z = 18, name = 'Ali', age = 25))






# Unpack input for LIST
#--------------------------------------------------

print('\n \n# Unpack input ---------------------------')
def my_sum(*args):
  print(args)
  total = 0
  for i in args:
    total += i

  return total

li = [1, 2, 3, 4, 5, 6, 7]
# x = my_sum(li)
x = my_sum(*li)
print(x)





# Unpack input for DICTIONARY
#--------------------------------------------------

def display_name(name, family):
  print(f"Hello {name} {family}")


display_name("Ali", "Akbari") # Hello Ali Akbari


person = {
  "name": "Ali",
  "family": "Akbari"
}

display_name(*person)  #send key and values
# Hello Ali Akbari
# Hello name family

display_name(**person)  # send keys only




# Lambda: a function without name that must be only one line
#--------------------------------------------------

# ordinary function
def my_square(x):
  print(x * x)
# single line function
def my_square(x): print(x * x)

# its lambda
val = lambda x: print(x * x)
val(5)

print(val.__name__)



# ordinary function: it is only in one line
def my_sum(x, y):
  print(x + y)
my_sum(10, 5)



# single line function
def my_sum(x, y): print(x + y)
my_sum(5, 5)



# lambda use case: when i want to call a function inside another function
# map: is a function that recieve a function and a iterable data(like set or list) , and do it
# map(func, iterable)
#--------------------------------------------------

# ordinary solution
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
double = []
for item in li:
  double.append(item * 2)
print(double)

# advanced solution
double = []
double = map(lambda item: item * 2, li)    # <map object at 0x10b54d210>
print(list(double))
print(list(double))




# simple example: Extraxt family form list of dict

users = [
  { "name": "Ali", "family": "Mahdavi", "age": 25},
  { "name": "Mina", "family": "Habibi", "age": 25},
  { "name": "Omid", "family": "Khoram", "age": 25},
  { "name": "Reza", "family": "Akbari", "age": 25},
]

families = []
for item in users:
  families.append(item['family'])

print(families)

print(list(map(lambda x: x["family"], users)))


















# for session 21
# -----------------------------------------
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
