class Kettel:

    dealer = "Big Bazaar"

    def __init__(self, make, price, discount, on):
        self.make = make
        self.price = price
        self.discount = discount
        self.on = on

    def swith_on_or_off(self, on):
        self.on = True

    def price_after_discoint(self):
        res = self.price  - ( self.price * (self.discount/100))
        return res

    def printDetails(self):
        print("Make : {}".format(self.make))
        print("Price : {}".format(self.price))
        print("Discount : {}".format(self.discount))
        print("Is it on ? : {}".format(self.on))
        print("*"*100)

if __name__=='__main__':

    k1 = Kettel("Hilton", 596.77, 10, False)

    k2 = Kettel("Prestige", 236.88, 20, False)

    k3 = Kettel("Samsung", 496.77, 50, False)

    k1.printDetails()

    k2.printDetails()

    k3.printDetails()

    print("Price after discount on kettel of make {} is {} ".format(k1.make, k1.price_after_discoint()))

    print("Price after discount on kettel of make {} is {} ".format(k2.make, k2.price_after_discoint()))

    print("Price after discount on kettel of make {} is {} ".format(k3.make, k3.price_after_discoint()))

    print(k1.__dict__)
    print(k2.__dict__)
    print(k3.__dict__)
    print(Kettel.__dict__)

    print("Dealer for all kettele is : {}".format(Kettel.dealer))

    print("#"*100)

    Kettel.guarentee = "6 months"
    k1.new_p = 100

    k1.dealer = "New dealer"

    k1.price = 0

    print(k1.__dict__)
    print(k2.__dict__)
    print(k3.__dict__)
    print(Kettel.__dict__)