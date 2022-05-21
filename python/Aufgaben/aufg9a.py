nArr = [6, 2, 2, 17, 23, 5, 2]
ind = 0
aNum = 2

for x in nArr:
    if x == aNum:
        print('number = ' + str(x) + ' at index ' + str(ind))
    ind += 1

ind = 0
print()
while ind < len(nArr):
    if nArr[ind] == aNum:
        print('number = ' + str(x) + ' at index ' + str(ind))
    ind += 1