'''
LAMBDA FUNCTION-
-A function without name (anonymous name)
-not powerful as named function
-it can work with single expression/ single line of code
'''


#named function-
def cal(a,b):
    return (a*a + 2*a*b + b*b)
print(cal(2,3))


#lambda function-
print((lambda a,b : a*a + 2*a*b +b*b)(2,3))