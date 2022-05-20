import mysql.connector
try:
	connection=mysql.connector.connect(host="mca107",user="mca107",password="mca107" database="mca107")
	cursor=connection.cursor()
	

while True:
	print("============SQL===========")
	print("1.create a table")
	print("2.insert")
	print("3.update")
	print("5.delete")
	print("6.exit")
	
	ch=int(input("Select a option"))
	if ch==1:
		try:
			q1=
	
