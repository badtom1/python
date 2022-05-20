while True:
	print("1.Copy the file")
	print("\n 0.Exit")

	ch=int(input("\nEnter Your Choice: "))
	if ch==1:
		try:
			a=input("Enter the Source File Name: ")
			a_mode=input("Enter the mode of the Source File: ")
			b=input("Enter the Destination File Name: ")
			b_mode=input("Enter the mode of the Destination File: ")
			f=open(a,a_mode)
			c=f.read()
			f1=open(b,b_mode)
			f1.write(c)
			print("File Copied Successfully")
		except TypeError:
			print("TypeError pls check \n")
		except FileNotFoundError:
			print("FileNotFound pls check \n")
		except ValueError:
			print("ValueError check \n")
		except IOError:
			print("IOError \n")
		except NameError:
			print("Your Error is Pls check the NameError \n ")
		except Exception as e:
			print("the Error is {}".format(e))
		finally:
			f.close()
			f1.close()
	else:
		break
		print("done")

