
queue = []

def addElem(elem):
    queue.append(elem)

def printQueue():
    print(queue)

def readElem():
    return queue.pop(len(queue) - 1)

if __name__ == '__main__':
    addElem('First Elem')
    addElem('Second Elem')
    printQueue()
    print(readElem())

    print('Enter elem')
    addElem(input())
    printQueue()