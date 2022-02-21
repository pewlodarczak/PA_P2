import array

anArray = array.array('i',[3,7,5,11,2,9,8])

for i in anArray:
    print(i)

anArray.insert(0,15)

for i in anArray:
    print(i)

