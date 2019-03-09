name  = input("Enter your name :")
address = input("Enter your address:")

salary = input("How much is your monthly salary ? ")
spent = input("How much you spent this month ?")
balance = float(salary) - float(spent)
message1 = "Hi, {0} , you are living in {1}. {0} your have spent {2} rupees this month. {0} your remaining balance is {3} rupees.".format(name,address,spent,balance)
message2 = "Note that your monthly salary is {0}".format(salary)
print(message1+message2)
