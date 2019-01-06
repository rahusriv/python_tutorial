from database import DataBase

class Product:

    def __init__(self):
        pass

    def initialize(self,product_id,product_name,category,price,quantity):
        #self.id = id
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity

    def insert(self):
        db = DataBase()
        sql = "INSERT INTO products (product_id, product_name, category, price, quantity) VALUES (%s, %s, %s, %s, %s)"
        values = (self.product_id,self.product_name,self.category,float(self.price),int(self.quantity))
        print(values)
        db.insertRowInTable(sql,values)

    def search(self,pattern):
        db = DataBase()
        sql = "SELECT * FROM products WHERE (product_name LIKE '%{}%')".format(pattern)
        value = db.selectRowFromTable(sql)
        return value


