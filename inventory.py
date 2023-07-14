from datetime import date
inventory = []
sales = []

def createInventory():
    inv = {}
    inv["pid"] = int(input("Enter the product id: ")) 
    inv["product"] = input("Enter the product name: ") 
    inv["category"] = input("Enter the product category: ")
    inv["quantity"] = int(input("Enter the product quantity: ")) 
    inv["price"] = int(input("Enter the price: ")) 
    inventory.append(inv)
    print(inventory)

def searchInventory(pname, pcat):
    product = [d for d in inventory if d['product'] == pname and d['category'] == pcat]
    filtered_product = dict((d['product'], d) for d in product)
    print(filtered_product)

def updateInventory(pname, pcat, ch):
    for x in inventory:
        if ch == 'b':
            amt = int(input("Enter the quantity bought: "))
            if x["product"] == pname and x["category"] == pcat:
                x["quantity"] += amt
                print(f"{amt} added to {x['product']} inventory")
        else:
            amt = int(input("Enter the quantity sold: "))
            if x["product"] == pname and x["category"] == pcat:
                sal = {}
                if x["quantity"] - amt >= 0:
                    x["quantity"] -= amt
                    print(f"{amt} deducted from {x['product']} inventory")
                    sal["product"] = x["product"]
                    sal["amt"] = amt
                    sal["tprice"] = amt * x["price"] 
                    sal["date"] = date.today()
                    sales.append(sal)
                    print(sales)

def displayInventory():
    for x in inventory:
        print("Product: "+x["product"])
        print("Quantity: "+str(x["quantity"]))
        print(" ")

def dailyReport():
    sale_amt = 0
    for x in sales:
        print("Product: "+x["product"]+" | Amount: "+str(x["amt"])+" | Price: "+str(x["tprice"])+" | Date: "+str(x["date"]))
        print(" ")
        sale_amt += x["tprice"]
    print("Total Sales for the day: "+ str(sale_amt))

def inventoryApp():
    print("******* Inventory App *******")
    print("1. Add product")
    print("2. Search Inventory")
    print("3. Display Inventory Details")
    print("4. Update Inventory")
    print("5. Daily sales Reports")
    print("6. Exit")
    opt = int(input("Select an option: "))
    match opt:
        case 1:
            createInventory()
        case 2:
            pname = input("Search for product: ")
            pcat= input("Enter product category: ")
            searchInventory(pname, pcat)
        case 3:
            displayInventory()
        case 4:
            pname = input("Enter the product: ")
            pcat= input("Enter product category: ")
            ch = input("Buy or Sale ? (b/s): ")
            updateInventory(pname, pcat, ch)
        case 5:
            dailyReport()
        case 6:
            exit()

cn = "yes"
while cn == "yes":
    cn = input("Do you want to use the inventory app ? (yes/no): ")
    if cn == "yes":
        inventoryApp()
    else:
        print("Inventory app closed!")
