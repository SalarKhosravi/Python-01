# print
# -------------------------------------------
#\n for line break, \t for tab
print("ali")
print("\t\t ali") # add tab at the begining
print("\t ali \n\n\n") # add tab and add two line break (inter) after print

# formating
name = "ali"
age = 35
print(f"my name is { name }, I am { age } years old")






# Other Type of variable
# -------------------------------------------
x = 3 #int
x = 3.1 #float
x = "Ali" #str
x = True #bool

x = [1, 2, 3, 4, 5] #list
x = { "apple", "banana", "orange"} #set
x = ("ali", "hassan", "sara") #tuple
x = {"name": "ali", "age": 32} #dictionary or Dict

print(type(x))






# Operators
# -------------------------------------------
x = 2 + 3   #add
x = 3 - 1   #minus
x = 3 * 3   #multiple
x = 25 / 5  #devide
x = 10 % 3 #remaining

print( 3 == 3) # equal
print(3 != 3)  # not eqaul
print( 3 > 2 )
print( 3 < 2 )
print( 3 <= 2 )
print( 3 >= 2 )




# input : to recieve a data from user in terminal
# -------------------------------------------
x = input("please insert a value: ")
print(x)
print(type(x))   # is always str, input is always str



age = input("please insert your age : ")
print(type(age))
age = int(age)
print(age)
print(type(age)) # We should change the input form string to integer





# if conditions
# -------------------------------------------
x = 1
if x == 1:
  print("x is one")


# syntax is as follow
#   if condistion :
#       statement
#   else:
#       another statement

# a simple project (insert a number between 1 to 5 and I tell you what you inserted in words)
x = input("insert a number between 1 to 5 : ")
x = int(x)
if x == 1:
  print("you inserted one")
elif x == 2:
  print("you inserted two")
elif x == 3:
  print("you inserted three")
elif x == 4:
  print("you inserted four")
elif x == 5:
  print("you inserted five")
else:
  print("it is not valid")





# range function
#syntax = range(start, end, step)
x = range(10)         # start from zero (no need to write), step one (no need to write)
print(list(x))        #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



x = range(4, 10)
print(list(x))       #[4, 5, 6, 7, 8, 9]      



x = range(0, 50, 5)
print(list(x))        #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]



x = range(20, 4, -2)
print(list(x))        #[20, 18, 16, 14, 12, 10, 8, 6]



x = range(10).__reversed__()
print(list(x))        #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]














# LOOP
# -------------------------------------------
# loop is a cycle where a piece of code run again and again
for i in range(10):
  print(i)




li = [ 10, 20, 30, 40 ]
for i in li:
  print(i)




name = "Ali Akbari"
for i in name:
  print(i)





# simple project: for 5 time, ask for an input then message on the input as words like bellow
for i in range(5):
  x = input("please ineter a number between 1 to 5: ")
  x = int(x)
  if x == 1:
    print(f"{ i }th : You inserted { x } which is one")
  elif x == 2:
    print(f"{ i }th : You inserted { x } which is two")
  elif x == 3:
    print(f"{ i }th : You inserted { x } which is three")
  elif x == 4:
    print(f"{ i }th : You inserted { x } which is four")
  elif x == 5:
    print(f"{ i }th : You inserted { x } which is five")
  else:
    print(f"{ i }th : It is not valid")

