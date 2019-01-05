import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = []

while(True):
    choice = input(" Enter data (Y)? or Exit (E)")

    if choice == "Y" or choice == "y":
        tmp = {}
        name = input(" Enter name : ")
        address = input(" Enter address :")
        tmp["name"] = name
        tmp["address"] = address
        mylist.append(tmp)
    else:
        break


x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)