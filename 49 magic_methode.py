class book():
    def __init__(self,name,color):
        self.name= name
        self.color=color

    def __str__(self):
        return (f"name={self.name}, color={self.color}")

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color


    def display(self):
        print(f"name={self.name}, color={self.color}")

b1=book("physics","blue")
b2=book("physics","red")


print(b1)
print(b1!=b2)