def gcd(a, b):
    if a == 0:
        return b
    else:
        while b != 0:
            if a > b:
                a = a - b
            else:
                b = b - a
    return a

a = 44
b = 12
print("gcd(", a , "," , b, ") = ", gcd(a, b))