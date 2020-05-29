# creating a simple class
class Employee:
    num_of_employees = 0
    amount_increment = 2.5

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.amount_increment = amount



print(Employee.num_of_employees)
emp_1 = Employee('Arc', 'Sena', 50000)

emp_2 = Employee('Bless', 'Gaza', 2000)


Employee.set_raise_amt(4.05)

emp_1.apply_raise()
print(emp_2.pay)
print(emp_1.pay)
