class Node:
    def __init__(self, isi):
        self.isi = isi
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, isi):
        a = Node(isi)
        if self.head is None:
            self.head = a
        else:
            a.next = self.head
            self.head = a

    def print_list(self):
        a = self.head
        while a is not None:
            print(a.isi, "->", end=" ")
            a = a.next
        print("None")

# Creating a linked list and adding elements
PrintLinkedList = LinkedList()
PrintLinkedList.add("Data 1")
PrintLinkedList.add("Data 2")
PrintLinkedList.add("Data 3")

# Printing the linked list
PrintLinkedList.print_list()
