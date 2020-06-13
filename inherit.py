class Voter:
    citizenship = "Ghanaian"


    def __init__(self, first, last, age, location):
        self.first = first
        self.last = last
        self.location = location
       

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @classmethod
    def condition(cls, temperature):
        pass
        

class DocumentNeeded:

    def __init__(self, passport, NIA):
        self.passport = passport
        self.NIA = NIA


class Eligibility(Voters):
    def __init__(first, last, age):
    super().__init__(first, last, age=None)
    self.age = age


    @staticmethod
    def eligible_to_vote(age):
        if age => 18:
            return True
        return False


