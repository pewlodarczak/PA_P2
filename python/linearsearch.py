cars = ["Tesla", "Ferrari", "Maseratti", "Lamborghini"]

aCar = "Ferrari1"

'''
i = 0
for x in cars:
    if x == aCar:
        print('Found: ' + aCar + ' ' + str(i))
    i += 1

for x in cars:
    if x == aCar:
        print('Found: ' + aCar + ' ' + str(cars.index(aCar)))
'''
indx = 0
try:
    indx = cars.index("Frr")
except Exception as e:
    print("Oops!", e.__class__, "occurred.")
    print("Entry not found.")
    print()
print('Found: ' + aCar + ' ' + str(indx))
