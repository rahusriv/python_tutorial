class Person:
    def __init__(self, f4, l5):
        self.f = f4
        self.l = l5

    def printname(self):
        print(self.f+" "+self.l)

class Student(Person):
    #def __init__(self, f, l):
    #    self.l = l
    #    self.f =f
    #    self.year  = "2019"
    def __init__(self,f1,l2):
        super().__init__(f1,l2)
        self.year = "2019"

x = Student("Mike", "Olison")
print(x.year)
print(x.printname())

x = Person("Mike", "Olison")
print(x)