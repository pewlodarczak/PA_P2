# Aufgabe 1

aVar1 = 1
aVar2 = 2
aVar3 = 3

sum = aVar1 + aVar2 + aVar3

print(sum)

# Aufgabe 2

aSizeMeter = 1.85
aSizeInch = 1.85 / 0.0254

print(str(aSizeMeter) + ' Meter')
print(str(aSizeInch) + ' Inches')

# Aufgabe 3
var1 = 9
var2 = 'Riproaring'

print(type(var1))
print(type(var2))

# Aufgabe 4
import math
r = 8
print(8*8*math.pi)

#r = input('Enter radius')
print(int(r)*int(r)*math.pi)

# Aufgabe 5
n = 0
print(n+(n*n)+(n*n*n))

# Aufgabe 6
arr = [8, 4, 9, 2]
print('Sum = ' + str((arr[0]+arr[1]+arr[2]+arr[3])))
biggest = 0
for x in arr:
    if x > biggest:
        biggest = x

print(biggest)

# Aufgabe 7
arr = [0, 2, 17, 23, 5, 7, 8, 26]
print(arr)
var1 = 5
var2 = 17
indx = 0
while indx < len(arr):
    if arr[indx] == var1:
        arr[indx] = var2
    elif arr[indx] == var2:
        arr[indx] = var1
    indx += 1
print(arr)
indx = 0
even = 0
odd = 0
for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print('Even: ' + str(even) + ' odd: ' + str(odd))

# Aufgabe 8
val1, val2 = 0, 1
nth = 0
arr = []
while val1 <= 13:
    print(val1)
    arr.append(val1)
    nth = val1 + val2
    val1 = val2
    val2 = nth

print(arr)

# Aufgabe 9
arr1 = [0, 2, 17, 23, 5, 7, 8, 26] 
arr2 = [8, 4, 9, 2] 
sumArr = arr1 + arr2
print(sumArr)
for x in sumArr:
    if x == 17 or x == 8:
        sumArr.remove(x)
print(sumArr)

# Aufgabe 10
arr = [2, 2, 17, 23, 5, 7, 8, 26, 7, 2]
count = 0
while count < len(arr):
    if arr[count] == 2:
        arr.remove(arr[count])
    else:
        count += 1
print(arr)

# Aufgabe 11
arr = [17, 23, 5, 7, 8, 26, 7, 8, 13, 43] 
print(arr)
arr.append(12)
print(arr)
arr.sort()
print(arr)
arr.reverse()
print(arr)

# Aufgabe 12
arr = [1, 5, 17, 23, 5, 7, 8, 26, 7, 8, 13] 
arr.sort()
print(arr[len(arr)-2])
arr.pop()
print(arr)