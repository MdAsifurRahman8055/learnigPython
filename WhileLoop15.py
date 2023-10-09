#While loop

i=2
while i<=10:
    print(i)
    i= (i+1)

# summation of n'th numbers
print("summation of n'th numbers")
n=int(input("Enter the n'th number:"))
sum=0
i=1
while i<=n:
    sum= sum+i
    i=i+1
print(sum)

#2+4+6+.....+n

sum=0
i=2
while i<=11:
    sum=sum+i
    i=i+2
print(sum)
# summation of inputed numbers
f=int(input("Enter your first number:"))
l=int(input("Enter your last number:"))
g=int(input("Enter your gaps between numbers:"))

sum=0
i=f
while i<=l:
    sum=sum+i
    i=i+g
print(sum)