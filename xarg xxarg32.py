#xarg

def add(*details):  # we used * to make al parameter works into one variable
    print(details)

add(96, "asif",5.00, "kzs")

# to sum some num togather
def s(*numbers):
    sum=0
    for x in numbers:
        sum = sum + x
    print(sum)

s(1,3,4,5,6,78,9)


#xxarg

def student(**details):  # for xxarg use **
    print(details)
    print(details["roll"])

student(roll=96, name="asif")