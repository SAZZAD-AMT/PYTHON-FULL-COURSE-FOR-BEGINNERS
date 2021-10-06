class Traingle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        area=0.5*self.base*self.height
        print("area of : ",area)

t1=Traingle(10,20)
t1.area()
t2=Traingle(30,20)
t2.area()