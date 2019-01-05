import mysql.connector

class DataBase:
    def __init__(self,host,user,passwd,database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )

    def insertRowInTable(self,sql,values):
        mycursor = self.mydb.cursor()
        mycursor.execut(sql,values)
        self.mydb.commit()