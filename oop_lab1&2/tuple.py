t1=(1,2,'abcd','xyz')
t2=(1,2,3,4,5)
print(t1)
print(t2)
while(True):
        print(" 1.length \n 2.concatenation \n 3.character in index \n 4.slicing \n 5.minimum \n 6.maximum \n 7.repeat n times\n 8.element present or no\n 9.find element \n 10.print \n 11.exit")
        choice=int(input("enter your choice\n"))
        if choice==1:
                print("length:",len(t1))
        elif choice==2:
                print(t1+t2)
        elif choice==3:
                index=int(input("enter index\n"))
                print(t1[index])
        elif choice==4:
                frm=int(input("enter from\n"))
                to=int(input("enter to "))
                print(t1[frm:to])
        elif choice==5:
                print(min(t2))
        elif choice==6:
                print(max(t2))
        elif choice==7:
                n=int(input("enter n numbers"))
                print(t1*n)
        elif choice==8:
                ch=int(input("enter element"))
                print(ch in t2)
        elif choice==9:
                ch=int(input("enter a element"))
                print(t2.count(ch))
        elif choice==10:
                print(t2)
        elif choice==11:
                break
        else:
                print("invalid choice")

