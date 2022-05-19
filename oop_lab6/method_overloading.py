#Method Overloading
class a:
	print("*********************METHOD OVERLOADING*******************")
	def hello(s, name=None, age=None):
		if(name!=None and age!=None):
			if(name.isalpha()):
				print("Hello",name,age)
			else:
				print("\n INVALID NAME")
		elif(name!=None):
			print("Hello",name)
		else:
			print("Hello")

obj=a()


while(True):
	print("\n 1.Enter Name and Age \n 2.exit")
	ch=int(input("\n Enter your choice:"))
	if(ch==1):
		name1=input("\n ENTER YOUR NAME-->")
		age1=input("\n ENTER YOUR AGE-->")
		if(name1 and age1):
			obj.hello(name=name1,age=age1)
		elif(name1):
			obj.hello(name=name1)
		elif(age1):
			obj.hello(age=age1)
		else:
			obj.hello()
	else:
		break

