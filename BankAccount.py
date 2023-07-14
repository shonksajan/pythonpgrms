accounts = {}

def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    accounts[account_number] = initial_balance
    print("Account created successfully!")

def withdraw():
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    if account_number in accounts:
        balance = accounts[account_number]
        if balance >= amount:
            accounts[account_number] = balance - amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def deposit():
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    if account_number in accounts:
        balance = accounts[account_number]
        accounts[account_number] = balance + amount
        print("Deposit successful!")
    else:
        print("Account not found!")

def exit_program():
    print("Exiting the program...")
   
    quit()

while True:
    print("1. Create Account")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    print("5.Invalid Choice")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        deposit() 
    elif choice == "4":
        exit_program()
    else:
        print("Invalid choice. Please try again.")