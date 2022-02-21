def BubbleSort(char_arr):
    iter = len(char_arr)
    while iter > 1:
        index = 0
        for i in char_arr:
            if i > char_arr[index+1]:
                j = i
                char_arr[index] = char_arr[index+1]
                char_arr[index+1] = j
            index+=1
            if index == len(char_arr) - 1:
                break
        iter-=1
    print(char_arr)

char_arr = ['f', 'e', 'z', 'd', 'h', 'b']
print(char_arr)
BubbleSort(char_arr)

# print(str(ord('f')) + " " + str(ord('e')))
"""
char_arr.sort(reverse=True)
print(char_arr)
"""
