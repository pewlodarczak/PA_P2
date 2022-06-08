import random

rand = random.randint(1, 15)
# print(rand)
if __name__ == '__main__':
    print('Guess a number between 1 - 15')
    guessNum = input()
    while int(guessNum) != rand:
        
        if int(guessNum) > rand:
            print('Number is smaller')
            print('Guess again')
            guessNum = input()
        else:
            print('Number is bigger')
            print('Guess again')
            guessNum = input()
    print('Correct: ' + str(rand))
    
    
    