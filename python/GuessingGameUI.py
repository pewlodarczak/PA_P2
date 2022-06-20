import random
from os import system
# from numpy import *

numArr = []
maxCol = 15

def createArray(maxNum):
    w, h = 0, 0
    if maxNum > maxCol:
        w = maxCol
        if maxNum % maxCol == 0:
            h = maxNum / maxCol
        else:
            h = (maxNum - (maxNum % maxCol)) / maxCol
            h += 1
    else:
        w, h = maxNum, 1
    #print('w: ' + str(w))
    #print('h: ' + str(h))
    
    numArr = [[0 for x in range(w)] for y in range(int(h))] 
    #print(numArr)
    
    r, c = 0, 0
    count = 1
    while r < h:
        while c < maxCol:
            if count < 10:
                numArr[r][c] = ' ' + str(count)
            else:
                numArr[r][c] = str(count)
            if count > maxNum and not c > maxCol - 1:
                numArr[r][c] = 'x'
                if c > maxCol - 1:
                    break

            c += 1
            count += 1
        r += 1
        c = 0

    for row in numArr:
        print(row)
    
def printNumbers(num, guess):
    #system('cls')
    
    createArray(num)

    count = 1
    while count <= int(num):
        if count <= int(guess):
            print('X', end = ' ')
            if count % 20 == 0:
                print()
        else:
            #print(str(count), end = ' ')              
            if count % 20 == 0:
                print()

        count += 1
    
if __name__ == '__main__':
    print('Enter a number between 1 - 500')
    maxNum = input()
    
    printNumbers(int(maxNum), 0)
    rand = random.randint(1, int(maxNum))
    #print(rand)

    print()
    print()
    print('Guess a number between 1 - ' + maxNum)
    guessNum = input()
    
    while int(guessNum) != rand:
        
        if int(guessNum) > rand:
            printNumbers(int(maxNum), int(guessNum))
            print()
            print('Number is smaller')
            print('Guess again')
            guessNum = input()
        else:
            print('Number is bigger')
            print('Guess again')
            guessNum = input()
    print('Correct: ' + str(rand))
    