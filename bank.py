class Bank:
    def __init__(self):
        self.balance = 0
        print("The account is created")


    def deposit(self):
        amount = float(input("Enter the amount to be deposit:"))
        print("Deposit is successful and the balance in the account is", amount + self.balance)
    
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw:"))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("The withdraw is successful and is", self.balance)
        else:
             print("Insufficient Balance")


    def enquiry(self):
        print("Balance in the account is ", self.balance)


acc = Bank()
acc.deposit()
acc.withdraw()