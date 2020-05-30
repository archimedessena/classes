#class Susu:
 #   amount_contributed_per_day = print(int(input("How much are you contributing per day?")))
 #   monthly_income = (amount_contributed_per_day * 20) - 50




   # def __init__(self, customer, location, contact):
   #     self.customer = customer
   #     self.location = location
   #     self.contact = contact

   # @staticmethod
    #def _constumer(first, last):
    #    first = last

        
class Customer:

    def __init__(self, first, last, contact, location):
        self.first = first
        self.last = last
        self.location = location
        self.contact = contact


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Contribution:
    amount_per_day = int(input("How much are you contributing on daily basis?"))
    monthly_income = amount_per_day * 20


    def __init__(self, annually, decade):
        self.annually = annually
        self.decade = decade


    
        


class Customer:

    def __init__(self, first, last):
        self.first = first
        self.last = last


    def fullname(self):
        return "{} {}".format(self.first + self.last)




class CashCollected:

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


    def Total_today(self):
        return 

