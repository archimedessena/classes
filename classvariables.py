class Employee:

    num_of_emps = 0
    raise_amount = 1.04 


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

        Employee.num_of_emps += 1



    
    def annual_salary(self):
        return f'{self.pay * 12}' 

    
    def decade_salary(self):
        return '{}'.format(self.pay * 12 * 10)

    



class CreditCard:


    def __init__(self, bank, customer, amount, account):
        self.bank = bank
        self.customer = customer
        self.amount = amount
        self.account = account


    def customer_credentials(self, first, last, pin):
        return 
        

    def name_of_bank(self):
        return self.bank # name of bank




    def _amount_(self):
        return self.amount




    def _account_(self):
        pass




news = Employee('sena', 'senadju', 1222)
print(Employee.num_of_emps)

