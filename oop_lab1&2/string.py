while(True):
        print("1.length\n2.character in index\n3.concatenation\n4.iteration\n5slicing\n6.uppercase\n7.repeat n times\n8.reverse the string\n9.count of characters\n10.character present or not\n11.exit")
        ch=int(input("enter your choice:"))
        if ch==1:
                str=input("enter your string:")
                print("length:",len(str))
        elif ch==2:
                str=input("enter your string:")
                index=int(input("enter the index:"))
                print(str[index])
        elif ch==3:
                str1=input("enter your first string:")
                str2=input("enter your second string:")
                print(str1+str2)
        elif ch==4:
                str=input("enter your string:")
                for i in str:
                        print(i)
        elif ch==5:
                str=input("enter your string:")
                frm=int(input("enter from:"))
                to=int(input("enter to:"))
                print(str[frm:to])
        elif ch==6:
                str=input("enter your string:")
                if(str.isalpha()):
                        print(str.upper())
                else:
                        print("invalid input:")
        elif ch==7:
                str=input("enter ypur string:")
                n=int(input("enter n times: "))
                print(n*str)
        elif ch==8:
                str=input("enter string:")
                print(str[::-1])
        elif ch==9:
                str=input("enter string:")
                char=input("enter character:")
                print(str.count(char))
        elif ch==10:
                a=input("enter string:")
                b=input("enter character:")
                print(b in a)
        elif ch==11:
                break
        else:
                print("invalid choice")

