# Python Tuples
# A tuple is a collection which is 
# ordered
# unchangeable
# duplicable

thistuple = ("apple", "banana", "cherry")
print(thistuple)


print(thistuple[1])
print(len(thistuple))


# One Item Tuple
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple") #NOT a tuple
print(type(thistuple))


# Tuple Items Data Types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))


# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



# Access Tuple Items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

print(thistuple[-1])
print(thistuple[-4:-1])
print(thistuple[-4:])

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")




# Update Tuples (cannot change, add, or remove items)
# -------------------------------------------------------------------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Add Items
# -------------------------------------------------------------------
# 1 append by list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# 2 combine two tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)




# Remove
# -------------------------------------------------------------------
# 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# 2
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists









# Pack & Unpack Tuples
# -------------------------------------------------------------------
x = 'Ali'
y = 'Sara'
z = 'Nika'

fruits = tuple((x, y, z)) # packing
print(type(fruits))
print(fruits)

# 1 unpacking
(a, b, c) = fruits
print('a: ' + a)
print('b: ' + b)
print('c: ' + c)

# 2 unpacking
(*newList, ) = fruits
print(newList)
print(type(newList))


# Unpack using *
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(x, *oth, y) = fruits
print(oth)





# Loop Tuples
# -------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
i = 1
while i < len(thistuple):
  print(thistuple[i])
  i += 1





#  Join Tuples
# -------------------------------------------------------------------

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)



fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


# Tuple Methods
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)