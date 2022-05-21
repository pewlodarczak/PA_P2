anArr = ['g', 2, 'o', 3, 'l', 1, 'e', 1, '.', 1, 'c', 1, 'm', 1]
print(anArr)
toRemove = 1
indx = 0
for x in anArr:
    if x == toRemove:
        anArr.pop(indx)
    indx += 1
        
print(anArr)