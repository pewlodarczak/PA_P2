key = 5
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def CaesarEncrypt(aStr):
    encr = []
    i = 0
    while i < len(aStr):
    # for i in range(len(aStr)):
        #print(aStr[i])
        if aStr[i] == ' ':
            # print('Blank')
            encr.append(' ')
            i += 1
            continue
        ind = alphabet.index(aStr[i])
        # print(ind)
        if ind + key > 26:
            encr.append(alphabet[key - (26 - ind)])
        else:
            # print(alphabet[ind + key])
            encr.append(alphabet[ind + key])
        i += 1
    #print(encr)
    return encr

aStr = input("Enter a string: ")
print(aStr)
enc = CaesarEncrypt(aStr)
str = " "
print(str.join(enc))

key = -5
enc = CaesarEncrypt(enc)
print(str.join(enc))
