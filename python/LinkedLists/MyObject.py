class Person():

    def __init__(self, nameArr):
        self.name = nameArr

    def __repr__(self):
        return str(self.name)

class PersonList():
    
    persons = []
    
    def listPersons(self):
        print(self.persons)
        
    def addPerson(self, name):
        self.persons.append(name)
    
    def __repr__(self):
        strRep = ''
        return str(self.persons)

persList = PersonList()
persList.addPerson(Person('Amanda'))
persList.addPerson(Person('Britney'))
persList.addPerson(Person('Sam'))

print(persList.listPersons())
