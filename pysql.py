import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="python_database"
)
mycursor = mydb.cursor()
# mycursor.execute("create table customer(name varchar(100),address varchar(250))")
mycursor.execute("show tables")
for i in mycursor:
    print(i)