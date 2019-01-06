from database import DataBase

class Order:

    def __init__(self):
        pass

    def initialize(self,phone_no,product_id,quantity):
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

    def getAllOrders(self,phone_no):
        db = DataBase()
        sql = """select *
from
    customers a
        inner join
    orders b
        on a.phone_no = b.phone_no
        inner join 
    products c
        on b.product_id = c.product_id
where a.phone_no = '{}';
""".format(phone_no)
        value = db.selectRowFromTable(sql)
        return value

