class a:
	def Hello(*a):
		l = len(a)
		if(l==1):
			print("Hello")
		elif(l==2):
			print("Hello ", a[1])
		elif(l==3):
			print("Hello ", a[1], a[2])
		else:
			print("only 2 arguments can be passed")

obj = a()
obj.Hello()
obj.Hello("Nithin", 22)
obj.Hello("Nithin")
obj.Hello("Nithin",22,34,45)
