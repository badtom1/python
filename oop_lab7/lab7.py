class employee():
        apply_raise=1.5
        def __init__(s,first,last,empid,salary):
                s.first=input("Enter your first name:")
                s.last=input("Enter your last name:")
                s.empid=input("Enter emp id:")
                s.salary=int(input("Enter salary:"))

        def display(s):
                print("First=",s.first)
                print("Last=",s.last)
                print("Emp id=",s.empid)
                print("Salary raise=",s.salary)

        def pay_raise(s):
                s.salary=(s.salary)*(s.apply_raise)
class developer(employee):
        apply_raise=2.5
        def pay_raise(s):
                s.salary=(s.salary)*(s.apply_raise)

class manager(employee):
        apply_raise=3.5
        def pay_raise(s):
                s.salary=(s.salary)*(s.apply_raise)
print("|---------enter employee details---------------|")
e1=employee("pavan","vc",101,200000)
print("|---------enter manager details----------------|_")
e2=manager("pannaga","ac",102,250000)
e1.pay_raise()
e2.pay_raise()
print("-----------------------------------------------|_")
e1.display()
e2.display() 

