string = "Ausnahmen bestätigen die Regel"

def toUpper():
    return string.upper()

def removeBlank():
    return string.replace(" ", "")

def revertString():
    return string[::-1]

def countE():
    eCount = 0
    for c in string:
        if c == 'e' or c == 'E':
            eCount += 1
    return eCount

def findStr(str):
    if string.find(str) >= 0:
        print('Found ' + str)
    else:
        print('Not found')

if __name__ == '__main__':
    string = toUpper()
    print(string)

    string = removeBlank()
    print(string)

    string = revertString()
    print(string)

    print(countE())

    print('Enter search string:')
    findStr(input())
