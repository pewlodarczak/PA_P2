def QueueDemo():
    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print("Initial queue")
    print(queue)

    print("Dequeue one element")
    queue.pop(0)
    print(queue)
    print("Dequeue one element")
    queue.pop(0)
    print(queue)

QueueDemo()