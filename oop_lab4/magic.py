from magic1 import*

ob1=op()
ob2=op()

ob1.accept()
ob2.accept()

while True:
	print("******************************************************************************")
	print("\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.FloorDivision\n 5.Exit")
	ch=int(input("enter your choice:"))
	print("******************************************************************************")
	if ch==1:
		ob1+ob2

	elif ch==2:
		ob1-ob2

	elif ch==3:
		ob1*ob2
    
	elif ch==4:
		ob1//ob2
    
	else:
		break
