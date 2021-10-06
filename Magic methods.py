class Bike():
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def __str__(self):
       return (f"Name = {self.name}, Color = {self.color}")

    def __eq__(self, other):
        return self.name== other.name and self.color==other.color

    def display(self):
        print(f"Name = {self.name},Color = {self.color}")


fz=Bike("FZ","Red")
ym=Bike("R1M","Blue")

print(str(fz))
print(fz==ym)
