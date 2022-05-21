class MyClass():
    x = "A man a plan a canal Panama"

    def __init__(self, x):
        self.x = x
        print('initializing')

    def output(self):
        return self.x

'''
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
'''

myClass = MyClass(7)

print(myClass.x)

class Node():
    nodes = []

    def __init__(self):
        self.node = None

    def addNode(self, node):
        self.nodes.append(node)

    def listNodes(self):
        for n in self.nodes:
            print(n)

    def __repr__(self):
        return "Node Object"

myNode = Node()
myNode.addNode(myClass)
# myNode.listNodes()
print()
myClass2 = MyClass(9)
print(myClass2.x)
myNode.addNode(myClass2)

myNode.listNodes()
print(myNode)

# del myClass2.x
# print(myClass2.x)
# del myClass2
