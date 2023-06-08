class Person():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def printFullName(self):
        print(self.firstName + self.lastName)

class Absolvent(Person):
    def __init__(self, firstName, lastName, abschlussjahr):
        super().__init__(firstName, lastName)
        self.abschlussjahr = abschlussjahr

    def berufsErfahrung(self):
        return 2023 - self.abschlussjahr
    
    def printNameWithAbschlussjahr(self):
        print(self.firstName, self.lastName, 'Abschlussjahr', self.abschlussjahr)

a = Absolvent('John', 'Doe', 2020)
print(a.berufsErfahrung())
a.printNameWithAbschlussjahr()