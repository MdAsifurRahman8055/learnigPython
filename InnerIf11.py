#find out the bigger number

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

if num1>num2:
    if num1>num3:
        print("num1")
    else:
        print("num3")

if num2> num1:
    if num2>num3:
        print("num2")
    else:
        print("num3")