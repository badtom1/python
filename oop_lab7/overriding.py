class employee():
	apply_raise=0.5
	def __init__(s,firstname,lastname,empid,salary):
		s.firstname=input("Enter your first name:")
		s.lastname=input("Enter your last name:")
		s.empid=input("Enter emp id:")
		while True:
			s.salary=input("Enter salary:")
			if(s.salary.isdigit()==False):
				print("Enter only numbers")
				
			else:
				continue;

	def display(s):
		print("Firstname is:",s.firstname)
		print("Lastname is:",s.lastname)
		print("Emp id is:",s.empid)
		print("Salary raise is:",s.salary)

	def pay_raise(s):
		s.salary=(s.salary)*(s.apply_raise)

class developer(employee):
	apply_raise=1.5
	def pay_raise(s):
		s.salary=(s.salary)*(s.apply_raise)
	
class manager(employee):
	apply_raise=2
	def pay_raise(s):
                s.salary=(s.salary)*(s.apply_raise)
print("_______________ENTER EMPLOYEE DETAILS_______________")
print("----------------------------------------------------")
e1=employee("n","j",1,5000)
print("\n")
print("_______________ENTER MANAGER DETAILS________________")
print("----------------------------------------------------")
e2=manager("p","v",2,70000)
print("\n")
e1.pay_raise()
e2.pay_raise()
print("__________EMPLOYEE SALARY RAISE___________")
print("-----------------------------------")
e1.display()
print("\n")
print("__________MANGER SALARY RAISE____________")
print("----------------------------------")
e2.display() 



