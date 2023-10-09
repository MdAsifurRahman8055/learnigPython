num=[10,20,30,40,50]
n=len(num)
"""
i=0
while i<n:
    print(num[i])
    i=i+1
"""
for x in num:# that's how we can print all the subject from list one bt one with for loop
    print(x)

#sum of the all subject of the list
sum=0
for x in num:
    sum=sum+x
print(sum)