from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()

def openLink(url):
    dll.insert(url)

def navigateBack():
    dll.goBack()

def navigateForward():
    dll.goForward()

if __name__ == '__main__':
    print(dll)
    print('Open URL slashdot.org')
    openLink('slashdot.org')
    print(dll)
    openLink('Nanoparticles')
    print(dll)
    openLink('Quantum Physics')
    print(dll)
    print(dll.goBack())
    openLink('Higgs Boson')
    print(dll)
    print(dll.goBack())
    print(dll.goBack())
    print(dll.goForward())

