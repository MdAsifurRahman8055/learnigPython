#And, Or , Not
num1=30
num2=40
num3=20

if num1>num2 and num1>num3:
    print("num1")
elif num2 > num1 and num2 > num3:
        print("num2")
else:
    print("num3")

#finding vowel
ch=input("Enter a latter:")

if ch=="a" or ch=="e" or ch=="i" or ch=="o"or ch=="u" or ch=="O"or ch=="I"or ch=="E"or ch=="A"or ch=="U":
    print("vowel")
else:
    print("consonant")