class Fruit:
    vegan = 1
    def __init__(self,taste,price,region):
        self.taste = taste
        self.price = price
        self.region = region

    def printFruit(self):
        self.vegan = 0
        print("Fruit is {}, it tastes {}, it is found in {}, its price is {}".format(Fruit.vegan, self.taste,self.region,self.price))

if __name__=='__main__':
    f1 = Fruit("sweet", 40, "north")
    f1.printFruit()
    print(f1.__dict__)
    print(Fruit.__dict__)