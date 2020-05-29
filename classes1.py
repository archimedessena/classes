class Cars:
   

    def __init__(self, amount, durability, origin, quality):
        self.amount = amount
        self.durability = durability
        self.origin = origin
        self.quality = self.durability and self.origin
       


    def select(self):
        #return ' {} {}'.format(self.durability, self.origin)
        return f'{self.durability} years durability and {self.origin} as origin'

    def amount_quality(self):
        return f'{self.amount} is the amount and is from {self.quality}'

    def below_average(self):
        dont = 500
        do = 45
        return (f'{dont} - {toyota}')


class Customers:


    def __init__(self, amount, destination):
        self.amount = amount
        self.destination = destination
        self.denied = f'{self.amount}' * 2


    def go_home(self):
        how_much_ = int(input("How much do u have?"))
        ans = how_much_
        if ans < 10000:
            return 'The price is 4000000'
        else:
            return 'You are in for a treat'

    
    def affairs(self):
        return f'{self.amount}' * 5


pricing = Customers(45000, 'Accra')
print(pricing.go_home())
print(pricing.amount)
