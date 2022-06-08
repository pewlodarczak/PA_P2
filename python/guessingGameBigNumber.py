import random

rand = random.randint(1, 500)
print(rand)
numberOfGuesses = 0
if __name__ == '__main__':
    print('Guess a number between 1 - 500')
    guessNum = input()
    while int(guessNum) != rand:
        numberOfGuesses += 1
        if int(guessNum) > rand:
            print('Number is smaller')
            print('Guess again')
            numberOfGuesses += 1
            guessNum = input()
        else:
            print('Number is bigger')
            print('Guess again')
            numberOfGuesses += 1
            guessNum = input()
    print('Correct: ' + str(rand))
    print('Guesses needed: ' + str(numberOfGuesses))
    
    
    