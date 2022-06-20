class Node:
    def __init__(self, song, path):
        self.data = song
        self.path = path
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def playNextSong():
        pass

llist = LinkedList()

first_node = Node('Beeth', 'c:\music\sym9.mp3')
second_node = Node("Moz")
third_node = Node("Erde")
forth_node = Node("Mars")
llist.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = forth_node
print(llist)

