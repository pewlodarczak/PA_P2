cars = ["Tesla", "Ferrari", "Maseratti"]

aCar = "Ferrari"

pos = 0

for x in cars:
    if x == aCar:
        print('Found: ' + aCar)
        print('Position: ' + str(pos))
    pos = pos + 1

