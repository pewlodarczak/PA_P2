cars = ["Tesla", "Ferrari", "Maseratti", "Lamborghini", "Ferrari"]
aCar = "Ferrari1"


i = 0
for x in cars:
    if x == aCar:
        print('Found: ' + aCar + ' ' + str(i))
    i += 1

for x in cars:
    if x == aCar:
        print('Found: ' + aCar + ' ' + str(cars.index(aCar)))
'''
'''
indx = 0
try:
    indx = cars.index(aCar)
except Exception as e:
    print("Oops!", e.__class__, "occurred.")
    print("Entry not found.")
    print()
print('Found: ' + aCar + ' ' + str(indx))

'''



def find(aCar, cars):
    global indx
    try:
        indx = cars.index(aCar)
        # print('Found: ' + aCar + ' ' + str(indx))
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Entry not found.")
        indx = 0
        print()
        
find(aCar, cars)
print('Found: ' + aCar + ' ' + str(indx))
