class a():
	def hello(self,name=None,age=None):
		if(name==None and age==None):
			print("hello , there")
		elif(name!=None and age==None):
			print("hello",' ',name)
		elif(name==None and age!=None):
			print("hello",' ',age)
		else:
			print("hello",' ',name,' ',age)
p=a()
p.hello()

while(True):
	print("\n 1.Enter Name and Age \n 2.exit")
	ch=int(input("\n Enter your choice:"))
	if(ch==1):
		name1=input("ENTER YOUR NAME-->")
		age1=int(input("ENTER YOUR AGE-->"))
		if(name1 and age1):
			p.hello(name=name1,age=age1)
		elif(name1):
			p.hello(name=name1)
		elif(age1):
			p.hello(age=age1)
		else:
			p.hello()
	else:
		break

