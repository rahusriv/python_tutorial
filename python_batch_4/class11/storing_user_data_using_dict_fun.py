
def moneySpentByCustomer(phone, customers):
    cust_data = customers[phone]
    shopping_dict = cust_data[3]
    sum = 0
    for key in shopping_dict:
        shopping_list = shopping_dict[key]
        for item in shopping_list:
            sum = sum + item[2] * item[3]
    return sum

def firstPurchase(phone,customers):
    first_item = ""
    if phone in customers:
        cust = customers[phone]
        shopping_dict = cust[3]
        if shopping_dict:
            first_shopping_cart = shopping_dict[1]
            if first_shopping_cart:
                first_item_data = first_shopping_cart[0]
                first_item = first_item_data[1]
                return first_item
    return first_item


def createData():
    customers = {}
    cust1 = ["mukund", 20,"HSR", {
        1: [[444,"moto e4", 10000,1],[555,"black shirt",1000,4],[666,"TV",20000,1]],
        2: [[222,"cricket bat",400,3],[777,"tennis ball",100,10]]},"prime"]

    cust2 = ["john", 50,"Koramangala", {
        1: [[22,"washing machine", 20000,2],[33,"shoes",900,5],[44,"Vegatables",20,10]],
        2: [[567,"bed",14000,2],[788,"car wash",800,1]],
        3: [[890,"sofa set",50000,1]]},"not prime"]
    customers[9611217325]= cust1
    customers[9611213490]= cust2
    return customers

def mainProgram():
    cust_dict = createData()
    user_phone_no = int(input("Enter you phone no : "))
    total_money_spent = moneySpentByCustomer(user_phone_no,cust_dict)
    first_item = firstPurchase(user_phone_no,cust_dict)
    name = cust_dict[user_phone_no][0]
    print("Hi, {} . Your first purchase was {} . Till now you have spent Rs {}".format(name,first_item,total_money_spent))

if __name__ == '__main__':
    mainProgram()







