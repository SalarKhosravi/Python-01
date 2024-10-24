# Variable Naming
# -----------------------------------------------------------------

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


a = 'Ali'
A = 'Ali' # This are different, python is case-sensitive meaning that these are two and are not equal (x != X)



# These are Ok
myvar = "Ali"
my_var = "Ali"
_my_var = "Ali"
myVar = "Ali"
MYVAR = "Ali"
myvar2 = "Ali"


# These cause Error
#    2myvar = "Ali"   # not allowed to start name with number
#    my-var = "Ali"   
#    my var = "Ali"  # space or dash is not acceptable









# Readable Name style
# -----------------------------------------------------------------

# Camel Case
myVariableName = "Ali"


# Pascal Case
MyVariableName = "Ali"


# Snake Case
my_variable_name = "Ali"









#  Assign Multiple Values
# -----------------------------------------------------------------

x, y, z = "Orange", "Banana", "Cherry"
print(x) # "Orange"
print(y) # "Banana"
print(z) # "Cherry"



x = y = z = "Orange"
print(x)
print(y)
print(z)









# Print Output
# -----------------------------------------------------------------

x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)



x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



x = 5
y = 10
print(x + y)



x = 5
y = "Ali"
# print(x + y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


x = 5
y = "Ali"
print(x, y)




# Python Numbers
# -----------------------------------------------------------------

x = 1    # int
y = 2.9  # float
z = 1j   # complex


# Type Conversion

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Python Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'










# Python Strings
# 'hello' is the same as "hello".

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Multiline Strings


a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)



# String Length
txt = "Hello, World!"
print(len(txt)) # 13


# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  