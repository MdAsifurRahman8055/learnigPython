#map

def cube(x):
    return x*x*x
num=[1,2,3,4,5,6,7,8]

result= list(map(cube,num))

print(result)

#filter
num=[1,2,3,4,5,6,7,8]

result=list(filter(lambda x: x%2==0,num))

print(result)
