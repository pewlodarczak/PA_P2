class Person():

    def __init__(self, name, salary):
        self.name, self.salary = name, salary
        
myPerson1 = Person('James', 70000)

print(myPerson1.name + ' ' + str(myPerson1.salary))
myPerson1.salary = 80000
print(myPerson1.name + ' ' + str(myPerson1.salary))

myPerson2 = Person('Jane', 70000)
print(myPerson2.name + ' ' + str(myPerson2.salary))
myPerson2.salary = 80000
print(myPerson2.name + ' ' + str(myPerson2.salary))
