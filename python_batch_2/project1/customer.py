from database import DataBase

class Customer:

    def __init__(self,name,address,phone_no,pwd,data):
        #self.id = id
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.pwd = pwd
        self.data = data

    def insert(self):
        db = DataBase()
        sql = "INSERT INTO customers (name, address, phone_no, pwd, data) VALUES (%s, %s, %s, %s, %s)"
        values = (self.name,self.address,self.phone_no,self.pwd,self.data)
        print(values)
        db.insertRowInTable(sql,values)

