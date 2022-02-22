import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='Nagasai@2002',
    port=3306
    )
mycursor = mydb.cursor()
mycursor.execute("use demo")
mycursor.execute("select * from demo_table")
for x in mycursor:
  print(x)