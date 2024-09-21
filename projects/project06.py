# Q: guess the number that pc randomly selected within a fix range of try

# simple solution
# ---------------------------------------------
# import random

# # Set the range of the number to guess
# number_to_guess = random.randint(1, 100)
# game_won = False

# print("I have selected a number between 1 and 100.")

# # Loop until the user guesses the number or runs out of attempts
# while game_won == False:
#     guess = input("Enter your guess: ")
#     if guess == 'end':
#         break

#     guess = int(guess)
#     if guess == number_to_guess:
#         game_won = True
#     elif guess < number_to_guess:
#         print("Too low!")
#     else:
#         print("Too high!")

# # Check if the game was won or lost
# if game_won:
#     print(f"Congratulations! You guessed the number.")












# Pro solution
# ---------------------------------------------

# import random

# # Set the range of the number to guess
# number_to_guess = random.randint(1, 100)
# attempts = 0
# max_attempts = 10
# game_won = False

# print("Welcome to the Guess the Number game!")
# print("I have selected a number between 1 and 100.")
# print(f"You have {max_attempts} attempts to guess it.")

# # Loop until the user guesses the number or runs out of attempts
# while attempts < max_attempts and not game_won:
#     guess = int(input("Enter your guess: "))
#     attempts += 1
    
#     if guess == number_to_guess:
#         game_won = True
#     elif guess < number_to_guess:
#         print("Too low!")
#     else:
#         print("Too high!")

# # Check if the game was won or lost
# if game_won:
#     print(f"Congratulations! You guessed the number in {attempts} attempts.")
# else:
#     print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")














# XPro solution
# ---------------------------------------------

import random

# Set the range of the number to guess
number_to_guess = random.randint(1, 100)
attempts = 0
game_won = False

game_hardness = int(input("Choose the difficulty level (easy: 1 \t Medium: 2 \t Hard: 3 \t VeryHard: 4): "))
if game_hardness == 1:
    max_attempts = 20
elif game_hardness == 2: 
    max_attempts = 10
elif game_hardness == 3: 
    max_attempts = 7
elif game_hardness == 4: 
    max_attempts = 4
else:
    print("input is not valid")


print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

# Loop until the user guesses the number or runs out of attempts
while attempts < max_attempts and not game_won:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == number_to_guess:
        game_won = True
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")

# Check if the game was won or lost
if game_won:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
else:
    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
