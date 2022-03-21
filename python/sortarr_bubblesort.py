def BubbleSort(num_arr):
    iter = len(num_arr)
    counter = 0
    while iter > 1:
        index = 0
        counter += 1
        change = False
        for i in num_arr:
            #print(i)
            #print(num_arr[index])
            if i > num_arr[index+1]:
                change = True
                #print(str(i) + " bigger than " + str(num_arr[index+1]))
                j = i
                num_arr[index] = num_arr[index+1]
                num_arr[index+1] = j
            # else:
                # print(num_arr[index+1] + " bigger than " + i)
                # print("Nothing to do")
            index+=1
            if index == len(num_arr) - 1:
                # print("break")
                #print(num_arr)
                break
        if  change == False:
             break    
        iter-=1
        change = True
    print(num_arr)
    print('Inerations: ' + str(counter))

# num_arr = [20, 8, 4, 7, 2, 5, 9, 3, 11, 2, 1, 1, 33, 0]
num_arr = [1, 2, 4, 7, 9, 11, 13, 15, 17, 20, 11, 21, 23, 35]
print(num_arr)

BubbleSort(num_arr)

# num_arr.sort(reverse=True)
# print(num_arr)

