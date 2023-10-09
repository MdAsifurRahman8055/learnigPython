n=input("Enter some numbers you want to sum up:")
list= n.split()#for split all string subjects from variable
sum=0
for num in list:
    sum = sum + int(num)
print(sum)#must use print function outside for loop


numLetter=0
numWord=0
numDigit=0
n=input("Enter a text:")
for x in n:
    x=x.lower()
    if x>='a' and x<='z':
        numLetter= numLetter+1
    elif x>='0' and x<='9':
        numDigit=numDigit+1
    elif x==' ':
        numWord= numWord+1
print("number of letters:",numLetter)
print("number of word:",numWord+1)
print("number of digit:",numDigit)
