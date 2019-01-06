from order import Order

def insertOrder(line):
    mylist = line.split(",")
    print(mylist)
    #product_id,product_name,category,price,quantity
    order = Order(mylist[0].strip(),mylist[1].strip(),mylist[2].strip())
    #print(cust)
    order.insert()

if __name__=='__main__':
    myfile = open("order_data.txt", "r")
    lines = myfile.readlines()
    for line in lines:
        insertOrder(line.strip())
        #print(line)