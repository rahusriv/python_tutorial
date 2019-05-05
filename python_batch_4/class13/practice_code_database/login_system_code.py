import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Python@12",
    database="mydb1"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address, phone_no, data, pwd) VALUES (%s, %s, %s, %s , %s)"
val = ("John", "Highway 21", "5555-6666", "I am john", "john@12")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")