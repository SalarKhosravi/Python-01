def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
    else:
        account['balance'] += amount
        account['transactions'].append(f"Deposited ${amount}")
        print(f"${amount} deposited successfully! Your new balance is: ${account['balance']}")

def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
    elif amount > account['balance']:
        print("Insufficient balance!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrew ${amount}")
        print(f"${amount} withdrawn successfully! Your remaining balance is: ${account['balance']}")

def display_balance(account):
    print(f"\nAccount Type: {account['type']}")
    print(f"Current Balance: ${account['balance']}")
    print(f"Transaction History:")
    if account['transactions']:
        for transaction in account['transactions']:
            print(f" - {transaction}")
    else:
        print("No transactions yet.")

def create_account():
    print("\nCreating a new account...")
    account_type = input("Choose account type (Checking/Savings): ").capitalize()
    if account_type not in ["Checking", "Savings"]:
        print("Invalid account type. Defaulting to Checking.")
        account_type = "Checking"
    
    owner = input("Enter the account owner's name: ")
    balance = float(input("Enter initial deposit amount: "))
    transactions = [f"Account created with initial deposit of ${balance}"]
    
    return {"owner": owner, "type": account_type, "balance": balance, "transactions": transactions}

def transfer(account_from, account_to, amount):
    if amount <= 0:
        print("Transfer amount must be greater than zero.")
    elif amount > account_from['balance']:
        print("Insufficient balance in the sending account!")
    else:
        account_from['balance'] -= amount
        account_to['balance'] += amount
        account_from['transactions'].append(f"Transferred ${amount} to {account_to['owner']}'s account")
        account_to['transactions'].append(f"Received ${amount} from {account_from['owner']}'s account")
        print(f"${amount} transferred successfully!")

def bank_account_simulator():
    print("Welcome to the Complex Bank Account Simulator!")
    
    accounts = {}
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Balance and Transactions")
        print("5. Transfer Money Between Accounts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            # Create a new account
            account = create_account()
            accounts[account['owner']] = account
            print(f"Account created successfully for {account['owner']}!")
        
        elif choice == "2":
            # Deposit money into an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    deposit(accounts[owner], amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Account not found.")
        
        elif choice == "3":
            # Withdraw money from an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    withdraw(accounts[owner], amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Account not found.")
        
        elif choice == "4":
            # Display balance and transaction history
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                display_balance(accounts[owner])
            else:
                print("Account not found.")
        
        elif choice == "5":
            # Transfer money between accounts
            sender_name = input("Enter your account owner's name: ")
            if sender_name in accounts:
                receiver_name = input("Enter the receiver's account owner's name: ")
                if receiver_name in accounts:
                    try:
                        amount = float(input("Enter the amount to transfer: "))
                        transfer(accounts[sender_name], accounts[receiver_name], amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("Receiver account not found.")
            else:
                print("Sender account not found.")
        
        elif choice == "6":
            # Exit the program
            print("Thank you for using the Bank Account Simulator! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the simulator
bank_account_simulator()