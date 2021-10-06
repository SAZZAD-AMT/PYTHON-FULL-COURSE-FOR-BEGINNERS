class a:
    def dis1(self):
        print("I am A")
class b():
    def dis2(self):
        print("I am B")
class c(b,a):
    def dis3(self):
        print("I am C")

a=c()
a.dis1()
a.dis3()
a.dis2()