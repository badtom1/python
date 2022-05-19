class op:
#Creating empty set
    def __init__(s):
        s.l1=[]
#Accepting input
    def accept(s):
        n=int(input("Enter the number of elements in a set:"))
        for i in range(0,n):
            e=int(input("Enter element: "))
            s.l1.append(e)
        print("list : ",s.l1)
#Addition of sets
    def __add__(s,other):
        newlist=[]
        for i in range(0,len(s.l1)):
            newlist.append(s.l1[i]+other.l1[i])
        print("After Addition : ",newlist)
#Subtraction of sets
    def __sub__(s,other):
        newlist=[]
        for i in range(0,len(s.l1)):
            newlist.append(s.l1[i]-other.l1[i])
        print("After Subtraction: ",newlist)
#Multiplication of sets
    def __mul__(s,other):
        newlist=[]
        for i in range(0,len(s.l1)):
            newlist.append(s.l1[i]*other.l1[i])
        print("After Multipication: ",newlist)
#divison of sets
    def __floordiv__(s,other):
        newlist=[]
        for i in range(0,len(s.l1)):
            newlist.append(s.l1[i]//other.l1[i])
        print("After Floor Division: ",newlist)
    
