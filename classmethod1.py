# Regular method always take self as the first argument
# But to change a regular method into  a class method is done by adding a decorator
# This take the class as the first argument
class Employee:
    num_of_emps = 0
    raise_amount = 1.04 
    raise_time = 3.5

    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 


    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    
    @classmethod
    def raise_well(cls, cash):
        cls.raise_time = cash


emp_1 = Employee('sena', 'senadju', 40000)
print(Employee.raise_well(3.5))

Employee.set_raise_amt((1.05))

print(Employee.raise_amount)
print(Employee.raise_well(3.5))
print(emp_1.raise_amount)