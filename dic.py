customer = []

def createAccount():
    account = {}
    cid = int(input("Enter your id: "))
    name = input("Enter your name: ")
    balance = int(input("Enter your balance: "))
    account['id']=cid
    account['name']=name
    account['balance']=balance
    customer.append(account)
    print(customer)

def deposit(cid, amt):
    for x in customer:
        if x['id'] == cid:
            x['balance'] += amt
    print(customer)
 
def withdraw(cid, amt):
    for x in customer:
        if x['id'] == cid:
            if(x['balance'] - amt >= 0):
              x['balance'] -= amt
            else:
                print(f"Minimum balance reached. You cannot withdraw {amt}") 
    print(customer)

def banks():
    print("*** MENU ***")
    print("1. Create Account") 
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    opt = int(input("Select an option: "))
    match opt:
        case 1:
            createAccount()
        case 2:
            cid = int(input("Enter the customer id: "))
            amt = int(input("Enter the amount to be deposited: "))
            deposit(cid, amt)
        case 3:
            cid = int(input("Enter the customer id: "))
            amt = int(input("Enter the amount to be withdrawn: "))
            withdraw(cid, amt)
        case 4:
            exit()
    
cn = "yes"
while cn == "yes":
    cn = input("Do you want to use the bank app ? (yes/no) : ")
    if cn == "yes":
        banks()
    else:
        print("Banking app closed")
    
    
    
    