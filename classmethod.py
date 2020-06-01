# creating a simple class
class Employee:
    num_of_employees = 0
    amount_increment = 2.5
 # regular classes
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@gmail.com'

        Employee.num_of_employees =+ 1

    def name_in_full(self):
        return '{} {}'.format(self.first, self.last) 


    def apply_raise(self):
        self.pay = int(self.pay * self.amount_increment)

     # using the class as an argument, it takes in cls as the first instance but regular methods takes in self as the first argument
     @classmethod
     def set_raise_amt(cls, amount):
         cls.amount_increment = amount


    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)



    # a static method does not take any argument from the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Arc', 'Sena', 50000)

emp_2 = Employee('Bless', 'Gaza', 2000)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

#emp_str_1 ='John-Doe-70000',
#emp_str_2 = 'Steve-Smith-30000',
##emp_str_3 = 'Jane-Doe-90000'

#new_emp_1 = Employee.from_string(emp_str_1)
#print(new_emp_1.email)
#print(new_emp_1.pay)
