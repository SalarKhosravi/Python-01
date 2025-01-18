# Compute guess the number in user mind between 1 and 100

low = 1
high = 100
tries = 0

while low <= high:
    guess = (low + high) // 2
    tries += 1
    response = input(f"Is your number {guess}? (enter 'up', 'down', or 'correct'): ").strip().lower()

    if response == 'correct':
        print(f"Yay! I guessed your number {guess} in {tries} tries!")
        break
    elif response == 'up':
        low = guess
    elif response == 'down':
        high = guess
    else:
        print("Please enter 'up', 'down', or 'correct'.")

if low == high:
    print(f"Your number must be {low}! I guessed it in {tries} tries!")
