import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="python_database"
)
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS college"
mycursor.execute(sql)