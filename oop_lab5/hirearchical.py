class student:
	def getdata(s):
		s.usn=input("Enter the USN:--> ")
		s.name=input("Enter the name of Student:-->")
		s.age=input("Enter the age:--> ")

	if age.isdigit()==True:
		s.age=int(s.age)
	
	else:
		print("\n\n Enter the Integer \n\n")
		s.age=input("Enter the Age \n ")

	def display(s):
		print("\n*******************STUDENT DETAILS*****************************\n")
		print("\n Name is %s \n USN IS %s \n age is %s:--> "%(s.name,s.usn,s.age))

class Ug(student):
	def ugdata(s):
		s.sem=input("Enter the Ug Sem:-->  ")
		s.fee=input("Enter the Fee:-->  ")
		s.stip=input("Enter the stiphend:-->  ")
	def display1(s):
		print("\n********** UG Fee Details **********\n")
		print("\n Sem is %s \n Fee is %s \n Stipend is %s"%(s.sem,s.fee,s.stip))
        
class pg(student):
	def pgdata(s):
		s.sem=input("Enter the Pg Sem:-->  ")
		s.fee=input("Enter the Fee:-->  ")
		s.stip=input("Enter the stiphend:-->  ")	
	def display2(s):
		print("\n********** PG Fee Details**********\n")
		print("\n Sem is %s \n Fee is %s \n Stipend is %s"%(s.sem,s.fee,s.stip))
u=Ug()
p=pg()

while  True:
	print("\n1.UG STUDENT \n2.PG STUDENT \n3.EXIT")
	ch=int(input("Enter the choice \n"))
	if ch==1:
		print("\n**********UGDATA**********\n")
		u.getdata()
		u.ugdata()
		u.display()
		u.display1()
	if ch==2:
		print("\n**********PGDATA**********\n")
		p.getdata()
		p.pgdata()
		p.display()
		p.display2()
	if ch==3:
		break

