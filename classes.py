# creating a simple class
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

#voqoxvmjhhgegjya
now = Employee('Archimedes', 'Senadju', 100000)
print(now.fullname())
#now1 = Employee('Jane', 'Stella', 300)
 


class Banku:

    def __init__(self, cassava, maize):
        self.cassava = cassava
        self.maize = maize
        self.gari = cassava + maize

    
    def ready(self):
        return '{} {}' .format(self.cassava, self.maize)


#print(now1.fullname())
#eat = Banku('Arc', 'Eli')
#print(eat.ready())
        
eat = Banku('neat', 'shitor')
print(eat.ready())