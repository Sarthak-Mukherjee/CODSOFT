print("MENUS\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
while True:
    ch=int(input("Enter ur choice[1-4]:"))
    
    if ch==1:
        print(a,"+",b,"=",a+b)
    elif ch==2:
        print(a,"-",b,"=",a-b)
    elif ch==3:
        print(a,"x",b,"=",a*b)
    elif ch==4:
        print(a,"/",b,"=",a//b)
    else:
        print("Invalid choice..")
        continue

    f=input("Do you want another calculation (y/n)?")
    if f=='n':
        print("THANK YOU!")
        break
    else:
        continue