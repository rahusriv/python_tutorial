from customer import Customer

def checkLogin():
    phone_no = input("Phone no :")
    pwd = input("Password :")
    cust = Customer()
    print(cust)
    res = cust.login(phone_no,pwd)
    print(res)
    cust.login = res
    print(cust.__dict__)
    res = cust.search("o")
    print(res)
    val = cust.getAllOrders()
    print(val)

if __name__=='__main__':
    checkLogin()