
class phone():  #parent class,base class,super class
    def call(self):
        print("you can call")
    def masseage(self):
        print("Masseage")

class iphone(phone): #subclass,child class
    """
     def call(self):
        print("you can call")
    def masseage(self):
        print("Masseage")
    """
    def cloud(self):
        print("you can use cloud")

s=iphone()
s.call()
s.cloud()
s.masseage()

print(issubclass(iphone,phone))