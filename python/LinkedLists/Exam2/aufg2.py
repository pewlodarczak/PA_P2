from queue import Queue

queue = Queue()

def addElem(elem):
    queue.put(elem)

def printQueue():
    print(list(queue.queue))

def readElem():
    return queue.get()

if __name__ == '__main__':
    addElem('First Elem')
    addElem('Second Elem')
    printQueue()
    print(readElem())

    print('Enter elem')
    addElem(input())
    printQueue()