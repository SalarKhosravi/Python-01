

# Arbitrary Keyword Arguments, **kwargs
def my_function7(**kid):
  print("His last name is " + kid["lname"])

my_function7(fname = "Tobias", lname = "Refsnes")






# Default Parameter Value
def my_function8(country = "Norway"):
	print("I am from " + country)

my_function8("Sweden")
my_function8()





# Passing a List 
def my_function9(food):
	print(type(food))
	print(food)
	for x in food:
		print(x)

fruits = ["apple", "banana", "cherry"]
my_function9(fruits)




# Return Values
def my_function10(x):
	return 5 * x

print(my_function10(3))




# PASS: do nothing
def my_function11(x):
	pass

my_function11






# Positional-Only Arguments or ONLY keyword arguments.
def my_function(x, /):
	print(x)

my_function(3)  # not x = 3


# Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)   # not 3









# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)






# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result

print("\n\nRecursion Example Results")
tri_recursion(6)







# Lambda
#---------------------------
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))




