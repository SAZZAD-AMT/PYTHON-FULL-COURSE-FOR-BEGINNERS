from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
  
    def area(self):
        pass

class Triangle(shape):
    def area(self):
        area=0.5*self.dim1 * self.dim2
        print("Triangle : ",area)

class rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("reactangle : ",area)

t=Triangle(10,20)
t.area()
r=rectangle(20,10)
r.area()