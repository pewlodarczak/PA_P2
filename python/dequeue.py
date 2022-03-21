from collections import deque

def QueueDemo():
    queue = deque()

    queue.append('a')
    queue.append('b')
    queue.append('c')
    queue.append('d')

    print("Initial queue")
    print(queue)

    print("Dequeue one element")
    queue.popleft()
    print(queue)
    print("Dequeue one element")
    queue.popleft()
    print(queue)

QueueDemo()