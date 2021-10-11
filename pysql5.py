import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="python_database"
)
mycursor = mydb.cursor()
# mycursor.execute("select * from customer")
# mycursor.execute("select name from customer")
mycursor.execute("select * from customer")
# myresult = mycursor.fetchall()
myresult = mycursor.fetchone()
for i in myresult:
    print(i)