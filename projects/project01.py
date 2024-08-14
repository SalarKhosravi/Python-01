# Input a number and answer if it is Prime Number or not



while True:
    # Ask the user to enter a number
    user_input = input("Enter a number (or type 'end' to stop): ")
    
    # Check if the user wants to end the program
    if user_input == 'end':
        print("Program has ended.")
        break
    
    number = int(user_input)
    
    # Check if the number is prime
    if number > 1:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"The number {number} is a prime number. \n\n")
        else:
            print(f"The number {number} is not a prime number. \n\n")
    else:
        print("The number should be greater than 1 to check for prime. \n\n")

