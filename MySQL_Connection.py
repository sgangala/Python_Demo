import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="rithwik", passwd="Rithwik@1",database="teekshanait")
mycursor = mydb.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchall()
for i in result:
    print(i)

print("Successful Connection")
