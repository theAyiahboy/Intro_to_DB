import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306, 
    user = "root",
    password = "Giov@nn1",
    database = "test_db"
)

if connection.is_connected():
    print("Connection to MySQL database was succesful!")

cursor = connection.cursor()

cursor.execute("SELECT DATABASE();")
record = cursor.fetchnone()
print("You're connected to database:", record)


cursor.close()
connection.close()
 