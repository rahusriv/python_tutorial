from order import Order

def insertProduct(line):
    mylist = line.split(",")
    print(mylist)
    #product_id,product_name,category,price,quantity
    product = Product(mylist[0].strip(),mylist[1].strip(),mylist[2].strip(),mylist[3].strip(),mylist[4].strip())
    #print(cust)
    product.insert()

if __name__=='__main__':
    myfile = open("order_data.txt", "r")
    lines = myfile.readlines()
    for line in lines:
        insertProduct(line.strip())
        #print(line)