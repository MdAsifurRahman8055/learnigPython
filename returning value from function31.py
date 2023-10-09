def add(x,y):
    sum= x+y
    return sum

result= add(4,6)
print("result",result)

#to find bigger num

def large(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
b= large(3333,2345,9345)
print(b)