import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Python@12"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydbtest")