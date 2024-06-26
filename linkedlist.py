class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Inisialisasi linked list
linked_list = LinkedList()

# Menambahkan data ke linked list
data = ["Ali", "Naik", "Kuda", "Sore", "Hari"]
for item in data:
    linked_list.add_node(item)

# Menampilkan isi linked list
linked_list.display()
