def myRange1(start = 0, end = 10, step = 1):
    i = start
    while i < end:
        print(i)
        i += step
            

myRange1(2, 40, 3)




def myRange(*args):
    start = 0
    step = 1
    if len(args) == 1:
        end = args[0]
    if len(args) == 2:
        start = args[0]
        end = args[1]
    if len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    
    # validation
    if end <= 0:
        print('end point can not be negative')
        return False
    
    if end < start:
        print('end point can not be smaler than start point')
        return False
    
    if step < 0:
        print('corrently we do not support negative step')
        return False

    # printing
    i = start
    while i < end:
        print(i)
        i += step
   

myRange(10)
myRange(2, 40)
myRange(2, 40, 5)
myRange(-3, 40, 5)
myRange(10, 30, -5)


