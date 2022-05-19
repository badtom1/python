d={}
class employee:
    def get_data(s):
        s.name=input("enter the name : ")
        s.empid=input("Enter the empid : ")
        s.address=input("enter the address : ")
        s.pan=input("Enter the pan : ")
        s.basic =int(input("Enter the basic salary : "))
        s.hra= s.basic*0.25
        s.da=s.basic*0.10
        s.gross=s.da+s.hra+s.basic
        if s.gross <250000:
            s.it= s.gross*0
        elif s.gross <500000:
            s.it =s.gross*0.10
        elif s.gross <1000000:
            s.it =s.gross*0.20
        else:
            s.it =s.gross*0.30
        s.pf=s.gross*.10
        s.con=3698
        s.deduct=s.it+s.pf+s.con
        s.net=s.gross-s.deduct
        s.update()
        print("\n\n______________________________________________________________________________________________________________")
    def  update(s):
        d.update({s.name:{"name":s.name , "gross":s.gross ,"Employee":s.empid,"Addres":s.address,"pan":s.pan,"basic:":s.basic,"hra":s.hra,"da":s.da,"it":s.it,"pf":s.pf,"deduct":s.deduct,"netsalary":s.net}})

    def search(s):
                name=input("enter the employee name: \n")
                count=0
                for k,v in d.items():
                        if (k==name):
                                print(d[name])
                                count=1
                if (count==0):
                        print("employee details not found: \n")

    def display(s):
        for key in d.keys():
            print("NAME : ",d[key]["name"])
            print("EMPLOYEE id : ",d[key]["Employee"])
            print("ADDRESS : ",d[key]["Addres"])
            print("PAN : ",d[key]["pan"])
            print("BASIC : ",d[key]["basic:"])
            print("HRA ",d[key]["hra"])
            print("DA ",d[key]["da"])
            print("IT",d[key]["it"])
            print("PF",d[key]["pf"])
            print("Gross",d[key]["gross"])
            print("Deduct",d[key]["deduct"])
            print("Netsalary",d[key]["netsalary"])
            print("\n\n")

while True:
	print("\n 1 . ADD EMPLOYEE DETAILS \n 2 . SEARCH \n 3 . DISPLAY \n 4 . EXIT ")
	ch=int(input("Enter the Choice :"))

	if ch==1:
		e = employee()
		e.get_data()
	if ch==2:
		e.search()
	if ch==3:
		e.display()
	if ch==4:
		break

