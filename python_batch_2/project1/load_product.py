from product import Product

def insertProduct(line):
    mylist = line.split(",")
    print(mylist)
    #product_id,product_name,category,price,quantity
    product = Product()
    #print(cust)
    product.initialize(mylist[0].strip(),mylist[1].strip(),mylist[2].strip(),mylist[3].strip(),mylist[4].strip())
    product.insert()

if __name__=='__main__':
    myfile = open("product_data.txt", "r")
    lines = myfile.readlines()
    for line in lines:
        insertProduct(line.strip())
        #print(line)