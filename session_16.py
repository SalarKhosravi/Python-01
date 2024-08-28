# Sets
# --------------------------------------------------------------
# set is unordered, unchangeable, unindexed, and do not allow duplicate values (but you can remove items and add new items.)
thisset = {"apple", "banana", "cherry"} # how to define
thisset = {1, 7, 5, 3, 4, 2, 6, 8} 
print(thisset) # unorder

# print(thisset[1]) #unindex

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"1", 1, True}
print(thisset)


# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"0", 0, False}
print(thisset)
print(len(thisset))
print(type(thisset))



# A set can contain different data types:
thisset = {"abc", 34, True, 40, "male"}
print(thisset)



# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



# Access Items
# --------------------------------------------------------------
# We can not use index as it is unorder and unindexed
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

print("banana" in thisset)
print("banana" not in thisset)



# Add Set Items
# cannot change its items, but you can add new items
# add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


# update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)



# Remove Item
# --------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")     # If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana")    # If the item to remove does not exist, discard() will NOT raise an error.
print(thisset) 



# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)



# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) #raise error








# Loop Sets
# --------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)





# Join Sets
# --------------------------------------------------------------
# There are several ways to join two or more sets in Python.
# 1- The union() and update() methods joins all items from both sets.
# 2- The intersection() method keeps ONLY the duplicates.
# 3- The difference() method keeps the items from the first set that are not in the other set(s).
# 4- The symmetric_difference() method keeps all items EXCEPT the duplicates.




# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set3 = set1 | set2
print(set3)





# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)




# Intersection
# Keep ONLY the duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
set3 = set1 & set2
print(set3)








#  it will change the original set 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)





# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3) #{False, True, 'apple'}





# Difference
# Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
set3 = set1 - set2
print(set3)




# difference_update
# Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)



# symmetric_difference()
# Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2
print(set3)



# symmetric_difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)









# Condition
# --------------------------------------------------------------
set1 = {"apple", "banana", "cherry"}
if 'apple' in set1:
  print('apple is here')

if not ('apple' not in set1):
  print('apple is here')



# Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print(x.issubset(y))
print(x <= y)


# Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
print(x.issuperset(y))
print(x >= y)


# check if there is any intersection
# Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
print(x.isdisjoint(y))
