class Salary:

    months_paid = 0
    monthly_increment = 20


    def __init__(self, day, month, year, pay):
        self.day = day
        self.month = month
        self.year = year
        self.pay = pay

        Salary.months_paid += 1


    def date_paid(self):
        return  '{}, {}, {}'.format(self.day, self.month, self.year)

    
    def increment(self):
        self.pay = int(self.pay *  self.monthly_increment)



Salary.monthly_increment
pay = Salary(1, 11, 1988, 4000)


pay1 = Salary(23, 2, 1788, 400000)

print(pay1.date_paid())

print(pay.month)





