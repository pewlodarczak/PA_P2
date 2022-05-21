num_arr = [20, 8, 4, 7, 2, 5, 9, 3, 11, 2, 1, 1, 33]

def evenAndOdd():
    numEven = 0
    numOdd = 0

    for x in num_arr:
        if x % 2 == 0:
            numEven += 1
        else:
            numOdd += 1

    print('Even: ' + str(numEven))
    print('Odd: ' + str(numOdd))

evenAndOdd()