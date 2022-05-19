while True:
	print("\n1.Copying the file")
	print("2.Check for Value Error")
	print("3.Check for Type Error")
	print("4.Check for I/O Error")
	print("5.Check for File Not Found Error")
	print("6.Check for Name Error")
	print("0.Exit")

	ch=int(input("\nEnter Your Choice: "))
	if ch==1:
		try:
			a=input("Enter the Source File Name: ")
			a_mode=input("Enter the mode of the Source File: ")
			b=input("Enter the Destination File Name: ")
			b_mode=input("Enter the mode of the Destination File: ")
			f=open(a,a_mode)
			c=f.read()
			f.close()
			f1=open(b,b_mode)
			f1.write(c)
			f1.close()
			print("File Copied Successfully")
		except FileNotFoundError:
			print("Encountered File Not Found Error")
		except ValueError:
			print("Encountered Value Error")

	elif ch==2:
		try:
			f=open("f1.txt","z")
			print("Successful")
		except ValueError:
			print("Encountered Value Error")
			print("Invalid Value Given")

	elif ch==3:
		try:
			f=open("f1.txt","w","r")
			print("Successful")
		except TypeError:
			print("Encountered Type Error")

	elif ch==4:
		try:
			f=open("f1.txt","w")
			f.write=("HI")
			f.close()
			print("Successful")
			f=open("f1.txt","r")
			f.write("HELLO")
		except IOError:
			print("Encountered Input/Output Error")
			print("The file which is opened in one mode is asked to perform the operation in another mode")

	elif ch==5:
		try:
			f=open("prakrthi.txt","r")
			f.read()
			print("Successful")
		except FileNotFoundError:
			print("Encountered File Not Found Error")

	elif ch==6:
		try:
			f=opens("f1.txt","w")
			print("Successful")
		except NameError:
			print("Encountered Name Error")
	elif ch==0:
		break

	else:
		print("Invalid Input")

