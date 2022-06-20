class Node:
    def __init__(self, musician, genre):
        self.musician = musician
        self.genre = genre
        self.next = None

    def __repr__(self):
        return self.musician

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.musician + ' ' + node.genre)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

llist = LinkedList()
print(llist)

first_node = Node("Mozart", "Classic")
llist.head = first_node
print(llist)

second_node = Node("Beatels", "Pop")
third_node = Node("Louis Armstrong", "Jazz")
first_node.next = second_node
second_node.next = third_node
print(llist)

