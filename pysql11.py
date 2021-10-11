import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database = "python_database"
)
mycursor = mydb.cursor()
 
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
mycursor.execute("SELECT * FROM student LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)