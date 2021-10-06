class student:
    roll=""
    gpa=""


    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"ROLL= {self.roll}\nGPA = {self.gpa}")

sazzad = student(143,3.82)
#print(isinstance(sazzad,student))
sazzad.display()


Tithi = student(1430,3.70)
#print(isinstance(sazzad,student))
Tithi.display()