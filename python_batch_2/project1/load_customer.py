from customer import Customer

def insertCustomer(line):
    mylist = line.split(",")
    print(mylist)
    #name,address,phone_no,pwd,data
    cust = Customer()
    cust.initialize(mylist[1].strip(),mylist[2].strip(),mylist[0].strip(),mylist[3].strip(),mylist[4].strip())
    #print(cust)
    cust.insert()

if __name__=='__main__':
    myfile = open("customer_data.txt", "r")
    lines = myfile.readlines()
    for line in lines:
        insertCustomer(line.strip())