#USERS
#{ id: 1, name: 'John', fav: 154},
#{ id: 2, name: 'Peter', fav: 154},
#{ id: 3, name: 'Amy', fav: 155},
#{ id: 4, name: 'Hannah', fav:},
#{ id: 5, name: 'Michael', fav:}

#PRODUCTS
#{ id: 154, name: 'Chocolate Heaven' },
#{ id: 155, name: 'Tasty Lemons' },
#{ id: 156, name: 'Vanilla Dreams' }
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)