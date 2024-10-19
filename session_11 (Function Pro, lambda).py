# Basic function
# def my_function():
# 	print("Hello from a function")

# my_function()



# Basic function with argument
#  ---------------------------------------------
# Ali is argument and fname is a parameter
# def my_function2(fname):
# 	print(fname + " Akbari")

# my_function2("Ali")



# Default Parameter Value
# ---------------------------------------------
# def my_function8(country = "Norway"):
# 	print("I am from " + country)

# my_function8("Sweden")
# my_function8()



# Arbitrary Arguments, *args
#  ---------------------------------------------
# def my_function3(*args):
# 	print(type(args))
# 	print(args)

# my_function3("Ali", "Reza", "Mohammad")
# data = ["Ali", "Reza", "Mohammad"]
# my_function3(*data)



# Arbitrary Keyword Arguments, **kwargs
# ---------------------------------------------
# def my_function7(**kwargs):
#   print(type(kwargs))
#   print("His last name is" , kwargs["fname"] , kwargs["lname"])

# my_function7(fname = "Reza", lname = "Asghari")

# data = {"fname": "Reza", "lname": "Asghari"}
# my_function7(**data)



# Passing a List 
# ---------------------------------------------
# def my_function9(food):
# 	print(type(food))
# 	print(food)
# 	for x in food:
# 		print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function9(fruits)




# simple Return Values
# ---------------------------------------------
# def my_function10(x):
# 	return 5 * x

# print(my_function10(3))




# PASS: do nothing
# ---------------------------------------------
# def my_function11(x):
# 	pass

# my_function11






# Positional-Only Arguments 
# ---------------------------------------------
# def my_function(x, /):
# 	print(x)

# my_function(3)  # not x = 3


# Keyword-Only Arguments
# ---------------------------------------------
# def my_function(*, x):
#   print(x)

# my_function(x = 3)   # not 3









# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
# ---------------------------------------------
# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)






# Recursion
# ---------------------------------------------
# Python also accepts function recursion, which means a defined function can call itself.

# def factorial(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * factorial(n-1)

# print(factorial(4))



# Lambda
# ---------------------------------------------
# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))



# order of function inputs
# ---------------------------------------------
# def my_function110(a, b, *args, var = 1, **kwargs):
# 	print(a, b, args, var, kwargs)

# my_function110(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, var = 11, name = "Reza", family = "Asghari")



# lambda function
# ---------------------------------------------
# def myFunc1(x, y): 
# 	return x + y

# def myFunc2(x, y): return x + y

# myFunc3 = lambda x, y : x + y
# print(myFunc3(1, 2))


