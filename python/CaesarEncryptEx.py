key = 5

def CaesarEncrypt(aStr):
    encr = ""
    for i in range(len(aStr)):
        char = aStr[i]
 
        if (char.isupper()):
            encr += chr((ord(char) + key-65) % 26 + 65)
 
        else:
            encr += chr((ord(char) + key - 97) % 26 + 97)
    return encr

aStr = input("Enter a string: ")
print(aStr)
enc = CaesarEncrypt(aStr)
print(enc)

key = -5
enc = CaesarEncrypt(enc)
print(enc)
