# Lösungs 1
anArr = ['g', 2, 'o', 3, 'l', 1, 'e', 1, '.', 1, 'c', 1, 'm', 1]

def numChar():
    numCharb = 0
    for x in anArr:
        if isinstance(x, str):
            numCharb += 1
    return numCharb

print(numChar())

# Lösungs 2
aArr = ['g', 2, 'o', 3, 'l', 1, 'e', 1, '.', 1, 'c', 1, 'm', 1]
numChar = 0

for c in aArr:
    if type(c) == str:
        numChar += 1
        
print('Number of characters: ' + str(numChar))