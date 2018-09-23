class Account(object):
    #account_number
    #name
    bank = "ICICI"
    branch = "MG Road Branch"
    ifsi_code ="ICICI0001"

    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def credit_money(self,amount):
        self.balance = self.balance + amount
        print("Deposited {} in your account".format(amount))

    def debit_money(self,amount):
        if(self.balance - amount < 0):
            print("You do not have enough balance")
        else:
            self.balance = self.balance - amount
            print("Amout debited")

class Customer:
    """This class will habe three variables
    name: string
    adhaar_no: string
    account : Instace/Object of Account Class
    """
    def __init__(self, name , adhaar_no, account_obj):
        self.name = name
        self.adhaar_no = adhaar_no
        self.account = account_obj

    def deposit(self, amount):
        self.account.credit_money(amount)

    def check_balance(self):
        return self.account.balance




if __name__=='__main__':
    mukund_account = Account("Mukund", "10001",10000)
    rahul_account = Account("Rahul","10002",10000)

    print("Balance for {} is {} ".format(mukund_account.name, mukund_account.balance))
    print("Balance for {} is {} ".format(rahul_account.name, rahul_account.balance))
    mukund_account.debit_money(500)
    print("Balance for {} is {} ".format(mukund_account.name, mukund_account.balance))
    rahul_account.debit_money(200)
    print("Balance for {} is {} ".format(rahul_account.name, rahul_account.balance))
    rahul_account.debit_money(10000)

    #mukund_account.bank = "HDFC"

    print(mukund_account.__dict__)
    print(rahul_account.__dict__)
    print(Account.__dict__)

    customer1 = Customer("mukund","1001",mukund_account)
    customer1.deposit(50000)
    print(customer1.check_balance())



