aStr = "The last message to earth"

def loopStr(str):
    for c in aStr:
        print(c)
    print()
    indx = 0
    while indx < len(aStr):
        print(aStr[indx])
        indx += 1

loopStr(aStr)
