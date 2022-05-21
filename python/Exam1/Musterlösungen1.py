# Aufgabe 3
arr = [2, 0, 2, 17, 23, 5, 7, 8, 26, 13, 15]
arr.sort()
arr.remove(arr[len(arr)-2])
print(arr)
arr.insert(5, 3)
print(arr)



# Aufgabe 6
str1 = 'Stecken'
str2 = 'pferd'

str1 += str2
print(str1)
print(str1.replace('Stecken', 'Renn', 1))
