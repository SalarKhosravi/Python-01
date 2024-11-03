# modules
# --------------------------------------------------
# import modules.dataFile
# x = modules.dataFile.products
# print(x)



# Naming a Module
# --------------------------------------------------
# import session_17 as s
# D = s.thistuple
# print(D)

# import modules.mymodule01 as x
# x.greeting("Jonathan")


# # Import From Module
# from modules.mymodule01 import greeting
# greeting("Jonathan")

# from modules.mymodule01 import *
# greeting("Jonathan")





# Map
# syntax: map(function, iterable) -> applies the function to each element of the iterable and returns a new iterable
# ---------------------------------------------
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myList2 = list(map(lambda x: x * 2, myList))
# print(myList2)

# myList3 = list(map(lambda x: x % 2 == 0, myList))
# print(myList3)


# myList = ['Ali', 'Mohammed', 2, 4, 'Ahmed', 8, 1.2, 'Omar', 'Khaled']
# myList4 = list(map(lambda x: x * 2 if type(x) == int else 0, myList))   
# print(myList4)



# Map for Dictionary   -> change (map) the elements of the dictionary based on the function
# ---------------------------------------------
# di = [
#     {'name': 'Ali', 'age': 20, 'city': 'Dubai'},
#     {'name': 'Mohammed', 'age': 25, 'city': 'Tehran'},
#     {'name': 'Khaled', 'age': 30, 'city': 'Baghdad'},
# ]

# names = list(map(lambda x: x['name'], di))
# print(names)








# Filter
# syntax: filter(function, iterable)  -> filters the elements of the iterable based on the function
# ---------------------------------------------
# di = [
#     {'name': 'Ali', 'age': 20, 'city': 'dubai'},
#     {'name': 'Mohammed', 'age': 25, 'city': 'tehran'},
#     {'name': 'Khaled', 'age': 30, 'city': 'tehran'},
#     {'name': 'Hamid', 'age': 22, 'city': 'rasht'},
#     {'name': 'Khosro', 'age': 36, 'city': 'esfahan'},
#     {'name': 'Sara', 'age': 17, 'city': 'tehran'},
# ]


# filteredNames = list(filter(lambda x: x['age'] > 26, di))
# print(filteredNames)

# tehranian = list(filter(lambda x: x['city'] == 'tehran', di))
# print(tehranian)




# Zip 
# Syntax: zip(iterable1, iterable2, ...) -> creates a list of tuples from the given iterables
# ---------------------------------------------
# li1 = [1, 2, 3, 4, 5]
# li2 = [6, 7, 8]
# li3 = list(zip(li1, li2))
# print(li3)



# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# print(list(zip(names, ages)))
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")



# .sort vs Sorted
# syntax: sort(iterable, key=None, reverse=False) -> sorts the elements of the iterable based on the key
# --------------------------------------------- 
# li = [3, 8, 10, 2, 4, 9, 1, 7, 18, 20, 12, 5]
# print(sorted(li))
# print(li)  

# li.sort()
# print(li)  

# sort string
# ---------------------------------------------
# nameList = ['date', 'apple', 'cherry', 'banana']
# nameList.sort()
# print(nameList)

# print(sorted(nameList))
# print(nameList)  





# sort based on key
# ---------------------------------------------
# nameList = ['date', 'apple', 'cherry', 'banana', 'tea', 'cheesecake']
# nameList.sort(key=len)
# print(nameList)

# nameList.sort(key=len, reverse=True)
# print(nameList)




# Sorted
# ---------------------------------------------
# myList110 = ['date', 'apple', 'cherry', 'banana', 'tea', 'cheesecake']
# print(sorted(myList110, key=lambda x: x[1]))
# print(sorted(myList110, key=lambda x: len(x), reverse=True))



# di110 = [
#     {'name': 'Ali', 'age': 20, 'city': 'dubai'},
#     {'name': 'Mohammed', 'age': 25, 'city': 'tehran'},
#     {'name': 'Khaled', 'age': 30, 'city': 'tehran'},
#     {'name': 'Hamid', 'age': 22, 'city': 'rasht'},
#     {'name': 'Khosro', 'age': 36, 'city': 'esfahan'},
#     {'name': 'Sara', 'age': 17, 'city': 'tehran'},
# ]

# sortedAge = sorted(di110, key=lambda x: x['age'])
# for person in sortedAge:
#     print(person['name'])

# sortedCity = sorted(di110, key=lambda x: x['city'])
# for person in sortedCity:
#     print(person['name'])


# mix map and sort to create the name output
# ---------------------------------------------
# di110 = [
#     {'name': 'Ali', 'age': 20, 'city': 'dubai'},
#     {'name': 'Mohammed', 'age': 25, 'city': 'tehran'},
#     {'name': 'Khaled', 'age': 30, 'city': 'tehran'},
#     {'name': 'Hamid', 'age': 22, 'city': 'rasht'},
#     {'name': 'Khosro', 'age': 36, 'city': 'esfahan'},
#     {'name': 'Sara', 'age': 17, 'city': 'tehran'},
# ]
# names = list(map(lambda x: x['name'],
#                 sorted(di110, key=lambda x: x['age'])
#             ))
# print(names)


# tehranian = list(map(lambda x: x['name'], 
#                 filter(lambda x: x['city'] == 'tehran', di110)
#             ))
# print(tehranian)


# ages = list(map(lambda x: x['age'], di110))
# averageAge = sum(ages) / len(ages)
# print(averageAge)

