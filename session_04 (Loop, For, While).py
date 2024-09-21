
# Data Type
# ---------------------------------------
x = None # None type: is type of emptyness, when there is nothing it will be None
x =  ''     # this is not empty, it is no spave caharacter, it differents from None  




# Python Conditions and If statements
# ---------------------------------------------------
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


a = 33
b = 200
if b > a:
	print("b is greater than a")





# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")





# Short Hand If
if a > b: print("a is greater than b")


a = 2
b = 330
print("A") if a > b else print("B")


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")









# Combine two conditions

print(True and True)
print(True & True)

print(True or False)
print(True | False)

print(True and not False)
print(not False)






# and (check both conditions)
a = 200
b = 33
c = 500
if a > b and c > a:
	print("Both conditions are True")


# OR (check if any is true)
a = 200
b = 33
c = 500
if a > b or a > c:
	print("At least one of the conditions is True")





# NOT: The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
	print("a is NOT greater than b")



# Nested If
x = 41

if x > 10:
	print("Above ten,")
	if x > 20:
		print("and also above 20!")
	else:
		print("but not above 20.")






















# FOR with lists
# -------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)  

# FOR with str
for x in "banana":
	print(x)


# FOR with range
for i in range(10):
	print(i)

for x in range(2, 30, 3):
	print(x)





# Break Statement: leave the loop and break
for i in range(10,20):
	print(i)
	if(i == 15):
		break


# Continue : With the continue statement we can stop the current iteration of the loop, and continue with the next:
for i in range(20,30):
	if(i == 23):
		continue
	else:
		print(i)


# Pass: do nothing, just go ahead (put in the pass statement to avoid getting an error)
for x in [0, 1, 2]:
  pass

for i in range(201,205):
	if(i == 203): pass
	else: print(i)








# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
	print(x)
else:
	print("Finally finished!")





# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
	if x == 3:
		break
		print(x)
	else:
		print("Finally finished!")




# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
	for y in fruits:
		print(x, y)











# WHILE
# -------------------------------------------
i = 1
while i < 6:
	print(i)
	i += 1

# here i is the counter, remember to increment i, or else the loop will continue forever.


i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

# here if you use (continue) instead of break, then you will get the infinite loop









# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)






# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
	print(i)
	i += 1
else:
	print("i is no longer less than 6")	