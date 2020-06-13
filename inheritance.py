# Inheritance enables us to inherit attributes and methods from a parent class
class Employee:
    num_of_emps = 0
    amount_increment = 1.04 

    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 


    def apply_raise(self):
         self.pay = int(self.pay * self.amount_increment)


class Developer(Employee): # This inherit classes from the employee class
    amount_increment = 1.20 # increasing the pay of developers by ten percent, this changes does not have a effect on the parent class

    # creating subclass of the developer class
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp) 


    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)


    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# isinstance() tells us if an object is an instance of a class
#print(isinstance(mgr_1, manager))
# issubclass tells us if a class is subclass of another
#print(issubclass(Manager, Developer))



    

new_dev = Developer('Gaza', 'Sena', 55800, 'Python')
new_dev_1 = Developer('Chima', 'Acid', 599999, 'Java')

mgr_1 = Manager('Senadju', 'Godway', 50000, [new_dev_1])
print(mgr_1.add_emp(new_dev_1))
#print(new_dev.email)
#print(new_dev_1.prog_lang)
#print(new_dev_1.apply_raise())




#now = Developer('Archimedes', 'Senadju', 100000)
#print(now.fullname())
#print(now.email)
#print(help(Developer))
#now1 = Employee('Jane', 'Stella', 300)
#dev_1 = Developer('Arc', 'Sena', 404040)
#dev_2 = Developer('BB', 'Abi', 400000)
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

 




#class Bed(Wood):
 #   wood_price = 400
 #   discount = 1.2
    

 #   def __init__(self, wawa, sapele, mahogany):
  #      self.wawa = wawa
  #      self.sapele = sapele
  #      self.mahogany

   # @classmethod
   # def regular_customer(cls, price):
     #   if price > wood_price:
    #        return wood_price / 2

    #  else:
       #  return "You have made it"
