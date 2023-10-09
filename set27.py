#for set we use second brackets
num1={1,2,3,4,5,5}
num2=set([4,5,6,7,8])   #to convert a list into a set

print(num1)  #in set duplicate values will not be shown

num2.add(9) # to add into set
print(num2)

num1.remove(5)  #to remove from set
print(num1)

print(4 in num1)  # to check
print(6 not in num1)


#union of set
print(num1 | num2)

#intersection of set
print(num1 & num2)

#diferance
print(num1 - num2)