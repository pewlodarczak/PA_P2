class Node():
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

        def __repr__(self):
            return self.data

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.currentNode = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert(self, url):
        NewNode = Node(url)
        if self.head == None:
            self.head = NewNode
            return
        last = self.head
        while (last.next):
            last = last.next
            # print('last ' + str(last))
        NewNode.previous = last
        last.next = NewNode
        # print('last ' + str(last.next))
        # print('previous ' + str(last.previous))
        self.currentNode = last.next

    def goBack(self):
        if self.head == None:
            # print('Empty List')
            return 'Empty List'
        
        #last = self.head
        #while (last.next):
        #    last = last.next
        # print(last.previous)
        
        # print(self.currentNode.previous)
        self.currentNode = self.currentNode.previous
        return self.currentNode
        # print(self.currentNode)

    def goForward(self):
        return self.currentNode.next



