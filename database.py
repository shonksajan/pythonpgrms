import psycopg2
conn = psycopg2.connect(database ="jtech",user ="postgres",host ="localhost",password ="1234",port ="5432")

cursor = conn.cursor()

id = int(input("Enter the id:"))
name = input("Enter the product name:")
quantity = int(input("Enter the quantity:"))
price = float(input("Enter the price:"))
category_id = int(input("Enter the category id:"))
cursor.execute(f"update inventory set p_name ='{name}',quantity ={quantity} ,price ={price},category_id={category_id} where p_id= {id}")
conn.commit()

cursor.execute("Select * from inventory")
list = cursor.fetchall()
for x in list:
    print(f"{x[0]}  {x[1]} {x[2]}  {x[3]}  {x[4]}")

cursor.close()