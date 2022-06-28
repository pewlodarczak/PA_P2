from collections import deque

stack = deque()

def addElem(elem):
    stack.append(elem)

def printQueue():
    print(stack)

def readElem():
    return stack.pop()

if __name__ == '__main__':
    addElem('First Elem')
    addElem('Second Elem')
    printQueue()
    print(readElem())

    print('Enter elem')
    addElem(input())
    printQueue()