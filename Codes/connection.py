import mysql.connector
conn=mysql.connector.connect(host='localhost', username='root',password='a8400629408',database='mydata')
my_cursor=conn.cursor()

print("created")

import mysql.connector
conn=mysql.connector.connect(host='localhost', username='root',password='a8400629408',database='managment')
my_cursor=conn.cursor()

print("created")
