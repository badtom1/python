while True:
	print("______________________________________________________________________")
	print("\n 1.length \n 2.Union \n 3.Intersection \n 4.Difference \n 5.Symmetric_difference \n 6.add \n 7.pop \n 8.discard \n 9.issubnet \n 10.clear \n 11.exit")
	ch=input("Enter your choice:")
	if ch.isdigit()==True:
		ch=int(ch)
	else:
		print("Invalid choice")
	l1={'a','b','c','nithin','hassan'}
	l2={'english','kannada','hindi'}
	if ch==1:
		print(l1)
		print(len(l1))
	if ch==2:
		print(l1)
		print(l2)
		print(l1|l2)
	if ch==3:
		print(l1)
		print(l2)
		print(l1&l2)
	if ch==4:
		print(l1)
		print(l2)
		print(l1-l2)
	if ch==5:
		print(l1)
		print(l2)
		print(l1^l2)
	if ch==6:
		print(l1)
		a=(input("Enter the element:"))
		if a.isdigit()==True:
			a=int(a)
		l1.add(a)
		print(l1)	
	if ch==7:
		print(l1)
		print("popped item:"+str(l1.pop()))
		print(l1)
	if ch==8:
		print(l1)
		a=(input("enter the element to remove:"))
		l1.discard(a)
		print(l1)
	if ch==9:
		print(l1)
		print(l1.issubset(l2))
	if ch==10:
		print(l2)
		l2.clear()
		print(l2)
	if ch==11:
		break
			
