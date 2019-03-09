#This is a class definition
class Kettle(object):
    certification = "ISI"
    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def swithc_on(self):
        self.on = True


#Main program starts from here
kenwood = Kettle("Kenwood",200)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 500
print(kenwood.price)

hamilton = Kettle("Hamilton",300)

print("Models : {}={} , {}={} ".format(kenwood.make, kenwood.price,hamilton.make, hamilton.price))

print("Models : {0.make}={0.price}, {1.make}={1.price} ".format(kenwood,hamilton))


#Switch on the kettle
print(hamilton.on)
hamilton.swithc_on()
print(hamilton.on)

#Calling method from Class , with out creating an instance
Kettle.swithc_on(kenwood)
print(kenwood.on)

#Objects can be modified in python (Unlike Java and C++)
print("*"*80)
kenwood.power = 150
print(kenwood.power)

print("*"*100)

kenwood.certification = "ISO"
#print(Kettle.certification)
print(hamilton.__dict__)
print(kenwood.__dict__)
print(Kettle.__dict__)

"""

Class : Template for creating objects . All objects created using the same class will have same characterstics
Object : An instance of the class
Intantiate : Creating an insance of a class
Method : A functon defined in a class
Attribute : A variable bound to an instance of a class
self : Is a reference to the instance of the class
"""
