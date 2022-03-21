from queue import Queue
 
aQueue = Queue(maxsize=3)

def QueueDemo():
    
    print(aQueue.qsize())
    aQueue.put('a')
    aQueue.put('b')
    aQueue.put('c')
    aQueue.put('d') 
    print("\nFull: ", aQueue.full())
 
    print("\nElements dequeued from the queue")
    print(aQueue.get())
    print(aQueue.get())
    print(aQueue.get())
 
    print("\nEmpty: ", aQueue.empty())
 
    aQueue.put(1)
    print("\nEmpty: ", aQueue.empty())
    print("Full: ", aQueue.full())

QueueDemo()