charArr = ['r', 'i', 'p', 'r', 'o', 'a', 'r', 'i', 'n', 'g']

print(charArr)
def reverse(charArr):
    inx = 0
    last = len(charArr)-1
    while inx < len(charArr)/2:
        tmp = charArr[inx]
        charArr[inx] = charArr[last]
        charArr[last] = tmp
        inx += 1
        last -=1

reverse(charArr)
print(charArr)
