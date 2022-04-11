aStr = "The last message to earth"

def loopStr(aStr):
    #for c in aStr:
        #print(c)
    print()
    indx = 0
    while indx < len(aStr):
        #print(aStr[indx])
        indx += 1
    print()

    print("earth" in aStr)

    # find substring 1 Lösung
    aTxt = "gobbledygook"
    subStr = "gook"
    indx = 0
    while indx < len(aTxt)-3:
        if aTxt[indx:indx+4] == subStr:
            print("Found " + subStr + " at index " + str(indx))
        indx += 1

    # find substring 2 Lösung
    print(aTxt.find(subStr))

    txt = "A man a plan a canal Panama"
    if "canal" in txt:
        print("Yes, 'canal' is present.")

    if "river" not in txt:
        print("No, 'river' is not present.")

    txt = "gobbledygook"
    print(txt)
    txt = txt.replace("y", "i")
    print(txt)

    print(txt[:5])
    print(txt[5:10])

    car = "Tesla"
    print(car[:3])
    print(car[3:5])

    car = "Tesla is great"
    print(len(car)) # prints length of car
    print(car.upper()) # prints car in upper case
    print(car.lower())
    print(car.replace(" ", "")) # removes blanks

    aStr = "Dreh mal am Herd"
    tmpStr = aStr
    aStr = aStr.lower()
    aStr = aStr.replace(" ", "")
    anStr = aStr[::-1]
    if(aStr == anStr):
        print(tmpStr + " is palindrome")

loopStr(aStr)
