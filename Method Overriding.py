class phone():
    def __init__(self):
        print("I am phone class")


class iphone(phone):
    def __init__(self):
        super().__init__()
        print("I am i phone class")

s=iphone()
