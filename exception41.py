#to avoid errors
try:  #to put it under inspection
   list=[20,0,20]
   result= list[0]/list[3]

   print(result)
except ZeroDivisionError:  #to avoid any type of error and leave a command
    print("Divided by zero isn't acceptable")
except IndexError:
    print("this index isn't allowed")
finally:
         print("one piece is real")  #if we use this keyword it'll work even if there's a error


list=[20,0,20]
result2= list[0]/list[2]
print(result2)



try:
   num1=int(input("Enter a number:"))
   num2=int(input("Enter another num:"))
   result3= num1 * num2
   print(result3)
except (ValueError,ZeroDivisionError): # to avoid any float or string
    print("sorry you have to input a numbers only")


def men(age):
    if age<18:
        raise ValueError("you are not a voter")
    return "invalid age"
print(men(12))