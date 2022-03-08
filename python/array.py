import array
#from array import *

anArray = array.array('i',[3,7,5,11,2,9,8])

for x in anArray:
    print(x)

anArray.insert(0,15)

for x in anArray:
    print(x)

print(anArray)
del anArray[3]

print(anArray)

i = 0
while i < len(anArray):
    print(anArray[i])
    i += 1

print(anArray.__sizeof__())