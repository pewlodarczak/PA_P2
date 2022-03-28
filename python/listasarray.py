cars = ["Tesla", "Ferrari", "Maseratti"]
print(type(cars))
print(cars[2]) # prints Maseratti
cars[2] = 'Lamborghini' # Overwrites Maseratti

for c in cars:
    if c == 'Ferrari':
        break
    print('Found you: ' + c)

person = ['John', 'Do', 45]
print(person)
person.reverse()
print(person)

for x in person:
    print(x)


# print(cars[1])
print(len(cars))

for x in cars:
    print(x)

cars.append("Lamborghini") # add element

for x in cars:
    print(x)

cars.pop()

for x in cars:
    print(x)

print(cars)

cars.sort()

print(cars)

i = 0
while i < len(cars):
    print(cars[i])
    i += 1