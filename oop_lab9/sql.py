import mysql.connector
try:
	connection=mysql.connector.connect(host="172.16.34.46",user="mca107",password="mca107",database="mca107")
	cursor=connection.cursor()
	print(connection)
	q1="create table employee7(empid varchar(10) primary key , name varchar(10), salary int(10) )"
	cursor.execute(q1)
	q2="insert into employee7 values(111,'nithin',500000)"
	cursor.execute(q2)
	connection.commit()
	cursor.execute("select * from employee7")
	result=cursor.fetchall()
	print(result)
	#cursor.execute("delete from employee7 where empid='111' ")
	#connection.commit()
	cursor.close()
except mysql.connector.Error as e:
	print("failed",e)
finally:
	if connection.is_connected():
		connection.close
	print("connection closed")
