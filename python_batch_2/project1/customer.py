from database import DataBase
from product import Product
from order import Order

class Customer:

    def __init__(self):
        pass

    def initialize(self,name,address,phone_no,pwd,data):
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

    def signup(self):
        db = DataBase()
        sql = "INSERT INTO customers (name, address, phone_no, pwd, data) VALUES (%s, %s, %s, %s, %s)"
        values = (self.name,self.address,self.phone_no,self.pwd,self.data)
        print(values)
        db.insertRowInTable(sql,values)

    def login(self,entered_phone_no,entered_pwd):
        db = DataBase()
        sql = "SELECT * FROM customers WHERE (phone_no = '{}')".format(entered_phone_no)
        value = db.selectRowFromTable(sql)
        print(value)
        if(len(value)==0):
            return 0
        row = value[0]
        if row[3] == entered_pwd :
            self.initialize(row[0],row[1],row[2],row[3],row[4])
            return 1
        else:
            return 0

    def search(self,pattern):
        product = Product()
        res = product.search(pattern)
        return res

    def getAllOrders(self):
        order = Order()
        res = order.getAllOrders(self.phone_no)
        return res
