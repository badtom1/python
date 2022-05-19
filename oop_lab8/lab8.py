print("|-----------------------------Welcome to oop lab----------------------|")
print("|----Demonstrating five exception handling mechanism using files------|")
while True:
        print("1->copy the file")
        print("2->check for value error")
        print("3->check for IO error")
        print("4->check for Name error")
        print("5->check for File not found error")
        print("6->check for Type error")
        print("7->Exit")
        ch=int(input("enter the choice-->"))
        if(ch==1):
                f=open("file1.txt",'r')
                g=open("file2.txt",'w')
                a=f.read()
                g.write(a)
                print("file copied")
        elif(ch==2):
                try:
                        g=open("file2.txt",'z')
                        print("successful")
                except ValueError:
                        print("g=open('file2.txt','z')")
                        print("Value error | because file open in unknown mode i.e <z>\n")
        elif(ch==2):
                try:
                        g=open("file2",'r')
                        print("successful")
                except IOError:
                        print("g=open('file2','r')")
                        print("IO Error | because the user havent specified the file extension i.e <file2.txt> \n")
        elif(ch==3):
                try:
                        g=opens("file2.txt",'r')
                        print("successful")
                except NameError:
                        print("g=opens('file2.txt','r')")
                        print("Name Error | use open keyword to <open> the file\n")
        elif(ch==4):
                try:
                        g=open("file3.txt",'r')
                        print("successful")
                except FileNotFoundError:
                        print("g=open('file3.txt','r')")
                        print("File not found Error | user accessing the notexisting file\n")
        elif(ch==5):
                try:
                        g=open("file2.txt",'r','w')
                        print("successful")
                except TypeError:
                        print("g=open('file2.txt','r','w')")
                        print("Type Error | user given two mode at a time\n")
        elif(ch==6):
                break;
        else:
                print("enter the correct choice")

f.close()
g.close()

