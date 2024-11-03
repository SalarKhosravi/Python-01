
# Importing the math module
print('---------------------------------------------------')
import math


# Working with constants
print('---------------------------------------------------')
print("Pi:", math.pi)         # The value of pi (3.14159...)
print("Euler's number:", math.e)  # The base of natural logarithms (2.71828...)



# Basic mathematical functions
print('---------------------------------------------------')
# Finding the square root
sqrt_val = math.sqrt(16)  # Square root of 16
print("Square root of 16:", sqrt_val)


# Power functions
pow_val = math.pow(2, 3)  # Equivalent to 2 ** 3
print("2 raised to the power of 3:", pow_val)



# Trigonometric functions (angle in radians)
print('---------------------------------------------------')
angle = math.pi / 4  # 45 degrees in radians
print("Cosine of 45 degrees:", math.cos(angle))
print("Sine of 45 degrees:", math.sin(angle))
print("Tangent of 45 degrees:", math.tan(angle))




# Converting between degrees and radians
print('---------------------------------------------------')
degrees = math.degrees(math.pi)  # Convert radians to degrees
radians = math.radians(180)      # Convert degrees to radians
print("180 degrees in radians:", radians)
print("Pi radians in degrees:", degrees)




# Logarithmic functions
print('---------------------------------------------------')
log_val = math.log(10)           # Natural logarithm of 10
log10_val = math.log10(100)      # Base-10 logarithm of 100
print("Natural logarithm of 10:", log_val)
print("Base-10 logarithm of 100:", log10_val)




# Rounding up and down
print('---------------------------------------------------')
ceil_val = math.ceil(4.3)        # Rounds up to the nearest integer
floor_val = math.floor(4.7)      # Rounds down to the nearest integer
print("Ceiling of 4.3:", ceil_val)
print("Floor of 4.7:", floor_val)



# Absolute value
print('---------------------------------------------------')
abs_val = math.fabs(-5)          # Absolute value of -5
print("Absolute value of -5:", abs_val)




# Factorial of a number
print('---------------------------------------------------')
factorial_val = math.factorial(5)  # 5! = 5*4*3*2*1
print("Factorial of 5:", factorial_val)




# Greatest Common Divisor (GCD) of two numbers
print('---------------------------------------------------')
gcd_val = math.gcd(28, 35)  # Finds the GCD of 28 and 35
print("GCD of 28 and 35:", gcd_val)




# Working with infinity and NaN (Not a Number)
print('---------------------------------------------------')
print("Positive infinity:", math.inf)
print("Negative infinity:", -math.inf)
print("Not a number (NaN):", math.nan)

