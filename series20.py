#1+2+3+4+.......+n
n=int(input("Enter last number:"))
sum=0
for x in range(1,n+1,1):
    sum = sum + x
print(sum)

#2+4+6+8+.......+n
n=int(input("Enter last number:"))
sum=0
for x in range(2,n+1,2):
    sum = sum + x
print(sum)

#1^1+2^2+3^3+4^4+.......+n^n
n=int(input("Enter last number:"))
sum=0
for x in range(1,n+1,1):
    sum = sum + x*x
print(sum)

#1*2*3*4*.......*n
n=int(input("Enter last number:"))
sum=1# we can't use 0 on sum this time or else the sum will be 0
for x in range(1,n+1,1):
    sum = sum * x
print(sum)