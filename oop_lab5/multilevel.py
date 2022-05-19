class student:
    def getdata(s):
        print("\n********************ENTER THE DATA*********************\n")
        s.usn=input("Enter the USN number:--> ")
        s.name=input("Enter the Name:--> ")
        s.age=input("Enter the Age:--> ")
class marks(student):
    def getmarks(s):
        s.sub1=input("Enter the SUB1:--> ")
        s.s1=int(input("Enter the marks of %s:--> "%(s.sub1)))
        s.sub2=input("Enter the SUB2 ")
        s.s2=int(input("Enter the marks of %s:-->  "%(s.sub2)))
        s.sub3=input("Enter the SUB3:-->  ")
        s.s3=int(input("Enter the marks of %s:-->  "%(s.sub3)))
        s.sub4=input("Enter the SUB4:-->  ")
        s.s4=int(input("Enter the marks of %s:-->  "%(s.sub4)))
        s.sub5=input("Enter the SUB5:-->  ")
        s.s5=int(input("Enter the marks of %s:-->  "%(s.sub5)))
class reslut(marks):
    def Reslut(s):
        s.total=s.s1+s.s2+s.s3+s.s4+s.s5
        s.per=s.total/5
        print("\n\n***************INFORMATION OF STUDENT*****************\n")
        print("\n\n Name : %s \n USN : %s \n age : %s \n %s : %d \n %s : %d \n %s : %d \n %s : %d \n %s : %d \n Total : %d \n Percentage : %d  "%(s.name,s.usn,s.age,s.sub1,s.s1,s.sub2,s.s2,s.sub3,s.s3,s.sub4,s.s4,s.sub5,s.s5,s.total,s.per))
        if s.s1>=35 and s.s2>=35 and s.s3>=35 and s.s4>=35 and s.s5>=35 : 
            if s.per >85:
                print("RESULT : Distiction")
            elif  s.per>60:
                print("RESULT : First Class")
            elif s.per>50:
                print("RESULT : Second Class")
            elif s.per>36:
                print("RESULT : Third Class")
            elif s.per<35:
                print("Fail")
        else:
            print("Result : FAIL")

r=reslut()
r.getdata()
r.getmarks()
r.Reslut()

