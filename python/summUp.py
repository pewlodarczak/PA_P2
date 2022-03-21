num_arr = [1, 2, 4, 7, 9, 11, 13, 15, 17, 20, 11, 21, 23, 35]

def sumUp():
    nsum = 0
    #for i in num_arr:
    #    nsum += i
    
    i = 0
    while i < len(num_arr):
        nsum += num_arr[i]
        i +=1
    print(nsum)


sumUp()