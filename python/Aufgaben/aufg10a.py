animalArr = ['Lion', 'Elephant', 'Dolphin', 'Shark', 'Cat']

animal1 = 'Elephant'
animal2 = 'Dolphin'

ind = 0

print(animalArr)
for a in animalArr:
    if animalArr[ind] == animal1:
        animalArr[ind] = animal2
    elif animalArr[ind] == animal2:
        animalArr[ind] = animal1
    ind += 1
print(animalArr)