import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="python_database"
)
mycursor=mydb.cursor()
sql="INSERT INTO customer(name,address) VALUES(%s,%s)"
val=[
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
     ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"row inserted sucessfuly")