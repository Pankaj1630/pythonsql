import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306, 
    database="python_database"
)
mycursor = mydb.cursor()
sql = "DELETE FROM student WHERE address = 'Lowstreet 4'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Item deleted")