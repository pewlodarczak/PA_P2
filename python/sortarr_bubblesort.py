def BubbleSort(num_arr):
    iter = len(num_arr)
    while iter > 2:
        index = 0
        for i in num_arr:
            #print(i)
            #print(num_arr[index])
            if i > num_arr[index+1]:
                #print(str(i) + " bigger than " + str(num_arr[index+1]))
                j = i
                num_arr[index] = num_arr[index+1]
                num_arr[index+1] = j
            #else:
                # print(num_arr[index+1] + " bigger than " + i)
                #print("Nothing to do")
            index+=1
            if index == len(num_arr) - 1:
                # print("break")
                #print(num_arr)
                break
        iter-=1
    print(num_arr)

num_arr = [20, 8, 4, 7, 2, 5, 9, 3, 11, 2, 1, 1, 33]
print(num_arr)

BubbleSort(num_arr)
"""
num_arr.sort(reverse=True)
print(num_arr)
"""
