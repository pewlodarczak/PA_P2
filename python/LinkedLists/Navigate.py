from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()

def openLink(url):
    dll.insert(url)

def navigateBack():
    dll.goBack()

if __name__ == '__main__':
    print(dll)
    print('Open URL slashdot.org')
    openLink('slashdot.org')
    print(dll)
    openLink('Nanoparticles')
    print(dll)
    openLink('Quantum Physics')
    print(dll)
    # dll.goBack()
    openLink('Higgs Boson')
    print(dll)
    # dll.goBack()
    # dll.goBack()

