class Account(object):
    #account_number
    #name
    bank = "Icici"
    branch = "MG Road Branch"
    ifsi_code ="ICICI0001"
    balance = 10000

    def __init__(self,name,account_number):
        self.name = name
        self.account_number = account_number

    def credit_money(self,amount):
        self.balance = self.balance + amount

    def debit_money(self,amount):
        if(self.balance - amount < 0):
            print("You do not have enough balance")
        else:
            self.balance = self.balance - amount
            print("Amout debited")


if __name__=='__main__':
    mukund_account = Account("Mukund", "10001")
    rahul_account = Account("Rahul","10002")

    print("Balance for {} is {} ".format(mukund_account.name, mukund_account.balance))
    print("Balance for {} is {} ".format(rahul_account.name, rahul_account.balance))
    mukund_account.debit_money(500)
    print("Balance for {} is {} ".format(mukund_account.name, mukund_account.balance))
    rahul_account.debit_money(200)
    print("Balance for {} is {} ".format(rahul_account.name, rahul_account.balance))
    rahul_account.debit_money(10000)



