numArr = [7, 45, 3.56, 4, 2.34, 5.43]
numInt = 0
numFloat = 0

for x in numArr:
    if type(x) == int:
        numInt += 1
    if type(x) == float:
        numFloat += 1
        
print('Number of ints: ' + str(numInt))
print('Number of floats: ' + str(numFloat))