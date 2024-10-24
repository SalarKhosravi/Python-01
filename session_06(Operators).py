# Boolean Values
print('True => ', True)
print('False => ', False)

print('Hello => ', bool("Hello"))       # Hello =>  True
print('nothing => ', bool(""))          # nothing =>  False
print('15 => ', bool(15))               # 15 =>  True
print('0 => ', bool(0))                 # 0 =>  False
print('None => ', bool(None))           # None =>  False








# Comparison Operators
# ----------------------------------------- 
print(10 == 9)
print(10 != 9)

print(10 > 9)
print(10 < 9)

print(9 < 9)
print(9 <= 9)

#   ==  Equal
#   !=  Not equal
#   >	Greater than
#   <	Less than
#   >=  Greater than or equal to
#   <=  Less than or equal to










# Logical Operators
# ----------------------------------------- 
#   and =   Returns True if both statements are true                    (x < 5 and  x < 10)
#   or  =   Returns True if one of the statements is true               (x < 5 or x < 4)
#   not =   Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

print(10 > 9 & 11 < 12)         # (True & True)     => True
print(10 > 9 & 11 < 12)         # (True & False)    => False
print(10 < 9 & 11 > 12)         # (False & True)    => False
print(10 < 9 & 11 < 12)         # (False & False)    => False


print(10 > 9 or 11 < 12)         # (True | True)     => True
print(10 > 9 or 11 < 12)         # (True | False)    => True
print(10 < 9 or 11 > 12)         # (False | True)    => True
print(10 < 9 or 11 < 12)         # (False | False)    => False



# Not
x = not(9 > 8)
print(x)        # False

x = not(9 == 8)
print(x)        # True








# SemiFalse : Some Values are False
# ----------------------------------------- 
print(bool(False))          # False
print(bool(None))           # False
print(bool(0))              # False
print(bool(""))             # False
print(bool(()))             # False
print(bool([]))             # False
print(bool({}))             # False











# Membership Operators # in, not in
# ----------------------------------------- 
Mylist = ['apple', 'banana', 'cherry']


if 'apple' in Mylist:
    print('apple is here')
else:
    print('nothing')




if 'tomatos' not in Mylist:
    print('nothing')
else:
    print('tomatos founded')










# identity Operators
# ----------------------------------------- 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x


print('x: ', id(x))
print('y: ', id(y))
print('z: ', id(z))


if (x == y):
    print('x, y are equal')

if (x is y):
    print('x, y are the same identity')

if (x is z):
    print('x, z are the same identity')


x.append('cherry')
print(x)
print(z)


if (x is not y):
    print('x, y are not the same')








# Operator Precedence
# ----------------------------------------- 
print(100 + 5 * 3)


# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR