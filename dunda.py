class Voter:

    def __init__(self, first, surname, age, date_of_birth):
        self.first = first
        self.surname = surname
        self.age = age
        self.date_of_birth = date_of_birth

    def fullname(self):
        return "{} {}".format(self.first, self.surname)



    def dob(self):
        return self.date_of_birth

class Documents(Voter):
    passport = input("Do you have travelling passport?")
    if passport == "yes":
        print("You are eligible to register")
    else: 
        print("Go home and bring guarantor")

    def __init__(self, first, surname, age, date_of_birth, passport):
        super().__init__(first, surname, age, date_of_birth)
        self.passport = passport


    def _passport(self):
        return (input("What is your passport number?, Thank you for coming"))


vote = Voter("Archimedes", "Sena", 23, '1-11-1988')
#print(vote.fullname())
#print(vote.date_of_birth)
doc = Documents("Archimedes", "Sena", 23, '1-11-1988', "yes")
doc._passport()
    