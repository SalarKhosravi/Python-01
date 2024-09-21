# Creating a Function
def my_function():
	print("Hello from a function")

my_function()



#  function can have input
def my_function2(name):
	print(f"Hello {name} from a function")

my_function2("Reza")



# Parameters or Arguments?
def my_function3(name):				#Parameters
	print(f"Hello {name} from a function")

my_function3("Reza")  # ---> Arguments






#  function input can be any numbers
def my_function4(fname, lname):
	print(fname + " " + lname)

my_function4("Emil", "Refsnes")






# Arbitrary Arguments, *args
def my_function5(*args):
	print("The youngest child is " + args[2])

my_function5("Emil", "Tobias", "Linus")





# Keyword Arguments
def my_function6(child3, child2, child1):
	print("The youngest child is " + child3)

my_function6(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




