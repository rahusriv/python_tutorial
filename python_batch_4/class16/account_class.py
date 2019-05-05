class Account:
    #account_number
    #name
    bank = "ICICI"
    branch = "MG Road Branch"
    ifsi_code ="ICICI0001"

    def __init__(self,name1,account_number1,balance1):
        self.name = name1
        self.account_number = account_number1
        self.balance = balance1
        self.statemnt = []

    def credit_money(self,amount):
        self.balance = self.balance + amount
        print("Deposited {} in your account".format(amount))

    def debit_money(self,amount):
        if(self.balance - amount < 0):
            print("You do not have enough balance")
        else:
            self.balance = self.balance - amount
            print("Amout debited = {}".format(amount))

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

    def debit_balance(self,amount):
        self.account.debit_money(amount)




if __name__=='__main__':
    mukund_account_obj = Account("Mukund", "10001",10000)
    rahul_account_obj = Account("Rahul","10002",10000)
    #mukund_account.branch = "XYZ"
    #mukund_account.abc = "XYZ"
    print("Balance for {} is {} ".format(mukund_account_obj.name, mukund_account_obj.balance))
    print("Balance for {} is {} ".format(rahul_account_obj.name, rahul_account_obj.balance))
    mukund_account_obj.debit_money(500)
    print("Balance for {} is {} ".format(mukund_account_obj.name, mukund_account_obj.balance))
    rahul_account_obj.debit_money(200)
    print("Balance for {} is {} ".format(rahul_account_obj.name, rahul_account_obj.balance))
    rahul_account.debit_money(10000)

    #mukund_account.bank = "HDFC"

    print(mukund_account_obj.__dict__)
    print(rahul_account_obj.__dict__)
    print(Account.__dict__)

    mukund = Customer("mukund","1001",mukund_account_obj)
    mukund.deposit(50000)
    print(mukund.check_balance())
    print(mukund.debit_balance(1000))
    print(mukund.check_balance())



