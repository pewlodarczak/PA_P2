numArr = [32, 33, 7, 31, 9, 23, 4, 11, 32, 3, 15, 32]

# Lösungsvariante 1
# numArr.sort()
# print(numArr[len(numArr)-2])

# Lösungsvariante 2
biggestNum = 0
secondBiggestNum = 0

for x in numArr:
    
    if x > biggestNum:
        biggestNum = x
        
for x in numArr:
    if x > secondBiggestNum and x < biggestNum:
        secondBiggestNum = x
    
print(biggestNum)
print(secondBiggestNum)