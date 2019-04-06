customers = {}

cust1 = ["mukund", 20,"HSR", {
    1: [[444,"moto e4", 10000,1],[555,"black shirt",1000,4],[666,"TV",20000,1]],
    2: [[222,"cricket bat",400,3],[777,"tennis ball",100,10]]
},
         "prime"]

cust2 = ["john", 50,"Koramangala", {
    1: [[22,"washing machine", 20000,2],[33,"shoes",900,5],[44,"Vegatables",20,10]],
    2: [[567,"bed",14000,2],[788,"car wash",800,1]],
    3: [[890,"sofa set",50000,1]]
},
         "not prime"]

customers[9611218765]= cust1

customers[9611213490]= cust2

phone = int(input("What's your phone no :"))

#Find hoe much money a customer has spent

cust_data = customers[phone]
shopping_dict = cust_data[3]
sum = 0
for key in shopping_dict:
    shopping_list = shopping_dict[key]
    for item in shopping_list:
        sum = sum + item[2] * item[3]

print("{} you have shopped for Rs . {} ".format(cust_data[0], sum))


# Finding first purchase
shopping_list_key_1 = 1
if phone in customers:
    shopping_dict = customers[phone][3]
    if shopping_list_key_1 in shopping_dict:
        item1 = shopping_dict[shopping_list_key_1]
        print(item1[0][1])
    else:
        print("You have never shopped with us. Her are some exciting dicounts for you.")
else:
    print("Sorry could not find your details. Please create an account with us")
