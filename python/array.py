import array
#from array import *

anArray = array.array('i',[3,7,5,11,2,9,8])

for x in anArray:
    print(x)

anArray.insert(0,15)

for x in anArray:
    print(x)

# del anArray[3]

print(anArray)

print(anArray.__sizeof__())