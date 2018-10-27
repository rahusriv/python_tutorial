import pymongo


client = pymongo.MongoClient("mongodb+srv://kay:myRealPassword@cluster0.mongodb.net/test")
db = client.test