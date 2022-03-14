num = [21, 6, 17, 1]

print(num)

'''
def sort(num):
    if num[0] > num[1]:
        tmp = num[0]
        num[0] = num[1]
        num[1] = tmp
    if num[1] > num[2]:
        tmp = num[1]
        num[1] = num[2]
        num[2] = tmp
'''

def sort(num):
    indx = 0
    while indx < len(num) - 1:
        if num[indx] > num[indx + 1]:
            tmp = num[indx]
            num[indx] = num[indx + 1]
            num[indx + 1] = tmp
            indx += 1

sort(num)
print(num)
