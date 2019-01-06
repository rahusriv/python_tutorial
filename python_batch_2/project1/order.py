from database import DataBase

class Order:

    def __init__(self,phone_no,product_id,quantity):
        #self.id = id
        self.phone_no = phone_no
        self.product_id = product_id
        self.quantity = quantity

    def insert(self):
        db = DataBase()
        sql = "INSERT INTO orders (phone_no,product_id,quantity) VALUES (%s, %s, %s)"
        values = (self.phone_no,self.product_id,int(self.quantity))
        print(values)
        db.insertRowInTable(sql,values)
