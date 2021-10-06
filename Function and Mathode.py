class student :
    roll=""
    gpa=""
    def setvalue(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"ROLL= {self.roll}\nGPA = {self.gpa}")

sazzad = student()
#print(isinstance(sazzad,student))
sazzad.setvalue(143,3.82)
sazzad.display()


Tithi = student()
#print(isinstance(sazzad,student))
Tithi.roll=1430
Tithi.gpa=3.70
Tithi.display()