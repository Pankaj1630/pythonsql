import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="python_database"
)
# mycursor = mydb.cursor()
# sql = "select * from customer where name = 'anil sharma'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall() 
# # myresult = mycursor.fetchone()
# for i in myresult:
#     print(i)

mycursor = mydb.cursor()
sql = "select * from customer where name = %s"
nm=("anil sharma",)
mycursor.execute(sql,nm)
result = mycursor.fetchall()
for i in result:
    print(i)