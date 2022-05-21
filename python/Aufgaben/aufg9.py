nArr = [6, 2, 2, 17, 23, 5, 2]

def findNum(aNum):
    print(nArr.index(aNum))

    print()

    ind = 0
    counter = 0
    for x in nArr:
        if x == aNum:
            print(ind)
            counter += 1
        ind += 1
    print(counter)
    print()

    ind = 0
    while ind < len(nArr):
        if nArr[ind] == aNum:
            print(ind)
        ind += 1

findNum(2)