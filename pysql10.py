import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database = "python_database"
)
mycursor = mydb.cursor()

# sql = "UPDATE student SET address='Apple 4052' WHERE address='Apple st 652'"

sql = "UPDATE student SET address = %s WHERE address = %s"
val = ("sdgfsajh","	Valley 345")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"Address is changed")