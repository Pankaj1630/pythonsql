import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="python_database"
)
mycursor = mydb.cursor()
# mycursor.execute("create table student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("show tables")
for i in mycursor:
    print(i)