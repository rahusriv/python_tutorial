import mysql.connector
import base64

def getData(phone_no):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Python@12",
        database="mydbtest"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM customers WHERE phone_no ='{}'".format(phone_no)

    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def insert(sql, val):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Python@12",
    database="mydbtest"
    )
    mycursor = mydb.cursor()
    #sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    #val = ("John", "Highway 21")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def createNewUser():
    phone_no = input("Phone No: ")
    name = input("Name : ")
    addr = input("Address: ")
    pwd = input("Password: ")
    pwd_encoded = base64.b64encode(pwd.encode())
    data = input("Tell my about yourself : ")
    sql = "INSERT INTO customers (phone_no,name, address,pwd,data) VALUES (%s, %s,%s,%s,%s)"
    val = (phone_no,name,addr,pwd_encoded,data)
    insert(sql,val)

def loginAndShowData():
    phone_no = input("Phone No: ")
    pwd = input("Password : ")
    value1 = getData(phone_no)
    if not value1:
        print("User name or password dosent exist . Try again. ")
        return

    value = value1[0]
    print(value)
    stored_pwd = value[3]
    stored_pwd_encoded = base64.b64encode(pwd.encode())
    if(stored_pwd == stored_pwd_encoded):
        print("Login success")
        print(value[4])


choice = int(input("Sign up (1) or Login (2)"))

if choice ==1:
    createNewUser()
else:
    loginAndShowData()