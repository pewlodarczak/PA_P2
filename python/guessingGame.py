import random

from os import system


def printNumbers(num, guess):
    system('cls')
    count = 1
    while count <= int(num):
        if count % 20 == 0:
            print(str(count), end = ' ')
            print()
        else:
            print(str(count), end = ' ')

        count += 1
    
if __name__ == '__main__':
    print('Enter a number between 1 - 500')
    maxNum = input()
    
    printNumbers(maxNum, 0)
    rand = random.randint(1, int(maxNum))
    #print(rand)

    print()
    print()
    print('Guess a number between 1 - ' + maxNum)
    guessNum = input()
    
    while int(guessNum) != rand:
        
        if int(guessNum) > rand:
            #printNumbers(maxNum, int(guessNum))
            print()
            print('Number is smaller')
            print('Guess again')
            guessNum = input()
        else:
            print('Number is bigger')
            print('Guess again')
            guessNum = input()
    print('Correct: ' + str(rand))
        
    
    