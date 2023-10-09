#inbuild module
from math import pow  # we can use * instead of pow to import all the function from math
print(pow(2,4))


#selfcreated module
from area_module import triangle,rectangle  # here area_module is another file where we already made a triangle function

triangle(20,30)
rectangle(20,30)