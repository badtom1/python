while True:
    print("1.length\n2.concatnation\n3.max\n4.min\n5.sort\n6.append\n7.pop\n8.reverse\n9.insert\n10.clear\n11.exit\n12.slicing")
    ch=input("Enter the choice : ")
    if ch.isdigit()==True:
        ch=int(ch)
    else:
        print("invalid choice")
    l1=[1,2,3,4,5,6]
    l2=['a','e','o','i','u']

    if ch==1:
        print(l1)
        print(len(l1))
    if ch==2:
        print(l1)
        print(l2)
        print(l1+l2)
    if ch==3:
        print(l1)
        print(max(l1))
    if ch==4:
        print(l1)
        print(min(l1))
    if ch==5:
        print(l2)
        l2.sort()
        print(l2)
    if ch==6:
        print(l1)
        a=input("enter the value")
        if a.isdigit()==True:
            a=int(a)       
        l1.append(a)
        print(l1)
    if ch==7:
        print(l1)
        l1.pop()
        print(l1)
    if ch==8:
        print(l1)
        l1.reverse()
        print(l1)
    if ch==9:
        print(l1)
        a=(input("enter the position : "))
        if a.isdigit()==True:
            a=int(a)
        else:
            print("Invalid position")
            continue
        b=input("enter the value")
        if b.isdigit()==True:
            b=int(b)
        l1.insert(a,b)
        print(l1)
    if ch==10:
        l1.clear()
        print(l1)
    if ch==11:
        break
    if ch==12:
        a=(input("enter the position : "))
        if a.isdigit()==True:
            a=int(a)
        else:
            print("Invalid position")
            continue
        b=(input("enter the position : "))
        if b.isdigit()==True:
            b=int(b)
        else:
            print("Invalid position")
            continue
        if len(l1)>b:
            print(l1[a:b])
        else:
            print("invalid position")
   
