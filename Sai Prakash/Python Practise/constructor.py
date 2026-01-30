class Abc:


    def __new__(cls):
        print("constructor called")

    def __init__(self):
        print("In it called")

    def show(self):
        print("In show")

obj=Abc()
obj.show()

obj1=Abc.__new__(Abc)
obj1.show()