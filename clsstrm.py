def what_day_is_today(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return "is true"
    return "is not true"

import datetime
today = datetime.date(2020, 1, 6)
print(what_day_is_today(today))












class Product:
    budget = 1.02
    discount = 0.01


    def __init__(self, order, time, location, amount):
    self.order = order
    self.time = time
    self.location = location
    self.amount = amount

    
    def customer_location(self):
        return location


    @classmethod
    def regular_customer(cls, time):
        cls.discount = "{} {}".format(self.order + self.time


    @staticmethod
    def finished_goods(food):
        return "neat fufu"


