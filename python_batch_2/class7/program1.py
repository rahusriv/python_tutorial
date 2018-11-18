#Linux
#sudo apt-get update
#sudo apt-get install mysql-server
#sudo ufw allow mysql
#systemctl start mysql
#systemctl enable mysql
#/usr/bin/mysql -u root -p
#UPDATE mysql.user SET Password = PASSWORD('password') WHERE User = 'root';
#connecting to a database

import mysql.connector

mydb = mysql.connector.connect(
    host="ensembldb.ensembl.org",
    user="anonymous",
    passwd=""
)

print(mydb)