import mysql.connector

mydb = mysql.connector.connect(
    host="ensembldb.ensembl.org",
    user="anonymous",
    passwd="",
    database="EnsEMBL"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM assembly LIMIT 10")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)