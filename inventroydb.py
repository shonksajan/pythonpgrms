
import psycopg2
from datetime import date

conn = psycopg2.connect(
    database="jtech",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
)

cursor = conn.cursor()


def insertProduct():
    id = int(input("Enter the id: "))
    name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price: "))
    category_id = int(input("Enter the category id: "))

    cursor.execute(
        f"insert into inventory values({id}, '{name}', {quantity}, {price}, {category_id})"
    )
    conn.commit()

    displayInventory()


def displayInventory():
    cursor.execute("select * from inventory order by p_id")
    list = cursor.fetchall()
    for x in list:
        print(f"{x[0]} {x[1]} {x[2]}  {x[3]}  {x[4]}")


def displayInventoryById(product_id):
    cursor.execute(f"select * from inventory where product_id={id}")
    list = cursor.fetchall()
    for x in list:
        print(f"{x[0]} {x[1]} {x[2]}  {x[3]}  {x[4]}")


def updateProduct():
    id = int(input("Enter the id: "))
    name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price: "))
    category_id = int(input("Enter the category id: "))

    cursor.execute(
        f"update inventory set p_name='{name}', quanity ={quantity}, price={price}, category_id={category_id} where p_id={id}"
    )
    conn.commit()

    displayInventory()


def insertSales(product_id, quantity):
    sales_id = int(input("Enter the sales id: "))
  

    cursor.execute(
        f"insert into sales values({sales_id}, {product_id}, {quantity}, '{date.today()}')"
    )
    conn.commit()
    print("Sales successfully completed!")
    cursor.execute(f"select quanity from inventory where p_id={id}")
    quant = cursor.fetchall()
    remQ = quant[0][0] - quantity
    cursor.execute(
        f"update inventory set quanity ={remQ} where p_id={id}"
    )
    conn.commit()
    displaySales()


def displaySales():
    cursor.execute("select * from sales order by sid")
    list = cursor.fetchall()
    for x in list:
        print(f"{x[0]} {x[1]} {x[2]}  {x[3]}  {x[4]}")


def salesReport(sdate, edate):
    cursor.execute(
        f"select s.sid, i.p_name, (s.sales_quantity * i.price), s.sales_date from sales s inner join inventory i on s.pid = i.p_id where s.sales_date between '{sdate}' and '{edate}'"
    )
    list = cursor.fetchall()
    for x in list:
        print(f"{x[0]} {x[1]} {x[2]}  {x[3]}")



def main():
    while True:
        print("\n===== Inventory Management =====")
        print("1. Add inventory")
        print("2. Update Inventory")
        print("3. Display Product")
        print("4. Display Inventory")
        print("5. Insert Sales")
        print("6. Daily Sales Report")
        print("7. Exit")

        choice = int(input("Enter your choice (1-5): "))

        match choice:
            case 1:
                insertProduct()
            case 2:
                updateProduct()
            case 3:
                id = int(input("Enter the product id: "))
                displayInventoryById(id)
            case 4:
                displayInventory()
            case 5:
                id = int(input("Enter the product id: "))
                quantity = int(input("Enter the quantity sold: "))
                insertSales(id, quantity)
            case 6:
                sdate = input("Enter the starting date: ")
                edate = input("Enter the ending date: ")
                salesReport(sdate,edate)
            case 7:
                print("Exiting the program...")
                break


main()
cursor.close()