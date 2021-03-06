class Node:
    def __init__(self, musician):
        self.musician = musician
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
            nodes.append(node.musician)
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

first_node = Node("Brahms")
llist.head = first_node
print(llist)

second_node = Node("Elvis")
third_node = Node("Bieber")
first_node.next = second_node
second_node.next = third_node
print(llist)

