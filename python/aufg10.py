animalArr = ['Lion', 'Elephant', 'Dolphin', 'Shark', 'Cat']

def switchAnîm(anim1, anim2):
    index = 0
    print(animalArr)
    while index <  len(animalArr):
        if animalArr[index] == anim1:
            animalArr[index] = anim2
        elif animalArr[index] == anim2:
            animalArr[index] = anim1

        index += 1

    print(animalArr)

switchAnîm('Elephant', 'Dolphin')