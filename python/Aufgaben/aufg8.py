def buildFibon(numb):
    print(numb)
    i = 2
    fib = [0, 1]
    while i < int(numb):
        fib.append(fib[i-2] + fib[i-1])
        i += 1
    print(fib)

numb = input("Enter Fibonacci numbers: ")

buildFibon(numb)
