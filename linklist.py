
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # menambahkan elemen baru sebagai elemen terdepan
    # pada list
    def prepend(self, node):
        node.next = self.head
        self.head = node

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


list = LinkedList()

list.prepend(Node(1))
list.prepend(Node(2))
list.prepend(Node(3))
list.prepend(Node(4))
list.prepend(Node(5))

list.print_all() 