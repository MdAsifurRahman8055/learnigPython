from abc import ABC,abstractmethod


class shape():
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2


    @abstractmethod  #now we can use shape class only for other class's use,,we can't make any objecct for abstracted class
    def area(self):
        pass


class triangle(shape):
    def area(self):
        area=.5* self.dim1 * self.dim2
        print("area of triangle:",area)

class rectangle(shape):
    def area(self):
        area=self.dim2*self.dim1
        print("area of rectangle:",area)


t1=triangle(20,30)
t1.area()
r1=rectangle(20,30)
r1.area()