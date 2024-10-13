# definition of list
#  ------------------------------------------------------
li = [1, 2, 3, 4, True, 'Ali', [101, 102, [201, 202]]]

print(li[0]) # 1
print(li[2:8:2])
print(li[-2]) # Ali


li.append(5)            # add to the end
li2 = li.copy()         # create a copy
li.count(1)             # 2 because True is 1
li.index('Ali')         # find the index of Ali -> 5 if not error
li.pop()                # remove form the efn
li.insert(2, 'hassan')  # insert hassan in index 2
li.remove('Ali')        # delete the element Ali
li.reverse()            # reverse all data
li.clear()              # delar all data



# definition of set
#  ------------------------------------------------------
se = {1, 2, 3, 3, 4, 4, 5, 4, 4, True, 'Ali'}
print(se)

# Set methods
se.add(6)               # Add an element to the set
se.remove(3)            # Remove an element (raises KeyError if not found)
se.discard(10)          # Remove an element if present (no error if not found)
se.pop()                # Remove and return an arbitrary element
se.clear()              # Remove all elements from the set

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)           # Union of two sets
intersection_set = set1.intersection(set2)  # Intersection of two sets
difference_set = set1.difference(set2)  # Elements in set1 but not in set2
symmetric_difference = set1.symmetric_difference(set2)  # Elements in either set, but not both

# Other set methods
is_subset = set1.issubset(set2)        # Check if set1 is a subset of set2
is_superset = set1.issuperset(set2)    # Check if set1 is a superset of set2
is_disjoint = set1.isdisjoint(set2)    # Check if sets have no elements in common

# Copy a set
set_copy = set1.copy()

# Update methods
set1.update(set2)       # Add elements from set2 to set1
set1.intersection_update(set2)  # Keep only elements found in both sets
set1.difference_update(set2)    # Remove elements found in set2 from set1
set1.symmetric_difference_update(set2)  # Keep elements in either set, but not both




# definition of dict
#  ------------------------------------------------------
# Define a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements
print(my_dict['name'])  # Output: John

# Adding or modifying elements
my_dict['job'] = 'Engineer'  # Add a new key-value pair
my_dict['age'] = 31  # Modify an existing value

# Removing elements
removed_value = my_dict.pop('city')  # Remove and return the value for 'city'
del my_dict['job']  # Remove the 'job' key-value pair

# Dictionary methods
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs as tuples

# Check if a key exists
if 'name' in my_dict:
    print("Name exists in the dictionary")

# Get a value safely
age = my_dict.get('age', 0)  # Returns 0 if 'age' is not found

# Update the dictionary
other_dict = {'country': 'USA', 'language': 'English'}
my_dict.update(other_dict)  # Add or update key-value pairs from other_dict

# Clear the dictionary
my_dict.clear()

# Create a copy of a dictionary
original_dict = {'a': 1, 'b': 2}
dict_copy = original_dict.copy()

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}  # Creates {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Get the number of key-value pairs
dict_length = len(my_dict)

# Nested dictionaries
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}
print(nested_dict['person1']['name'])  # Output: Alice






# definition of tuple
# Note: Tuples are immutable, so methods like append(), extend(), remove(), etc. are not available
#  ------------------------------------------------------   
# Tuple definition and methods


# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("Original tuple:", my_tuple)

# Accessing elements
print("\nAccessing elements:")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("\nSlicing:")
print("Elements from index 2 to 4:", my_tuple[2:5])

# Length of a tuple
print("\nLength of the tuple:", len(my_tuple))

# Count occurrences of an element
print("\nCount of 'a' in the tuple:", my_tuple.count('a'))

# Find index of an element
print("\nIndex of 'b' in the tuple:", my_tuple.index('b'))

# Tuple unpacking
a, b, c, *rest = my_tuple
print("\nUnpacking the tuple:")
print("a =", a, "b =", b, "c =", c, "rest =", rest)

# Tuple concatenation
another_tuple = (4, 5, 6)
concatenated_tuple = my_tuple + another_tuple
print("\nConcatenated tuple:", concatenated_tuple)

# Tuple repetition
repeated_tuple = my_tuple * 2
print("\nRepeated tuple:", repeated_tuple)

# Check if an element exists in the tuple
print("\nIs 'a' in the tuple?", 'a' in my_tuple)

# Convert tuple to list
tuple_to_list = list(my_tuple)
print("\nTuple converted to list:", tuple_to_list)

# Convert list to tuple
list_to_tuple = tuple(tuple_to_list)
print("\nList converted back to tuple:", list_to_tuple)





