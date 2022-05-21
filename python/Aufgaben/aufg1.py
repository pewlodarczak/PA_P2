num = [21, 6, 17]

def sort(num):
    if num[0] > num[1]:
        tmp = num[0]
        num[0] = num[1]
        num[1] = tmp
    if num[1] > num[2]:
        tmp = num[1]
        num[1] = num[2]
        num[2] = tmp


sort(num)
print(num)