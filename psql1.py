<<<<<<< HEAD
=======
# This is the comment in the python
# This is second line comment
>>>>>>> second_branch
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="",
    port=3306
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE python_database")
mycursor.execute("show databases")
for i in mycursor:
    print(i)

