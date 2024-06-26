import os
# kelas node
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# kelas double
class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    # TAMBAH NODE
    def menuTambah(self):
        os.system('clear')
        temp = int(input('Masukkan data baru = '))
        new_node = Node(temp)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # HAPUS NODE
    def menuHapus(self):
        os.system('clear')
        temp = int(input('Masukkan data yang akan dihapus = '))
        current_node = self.head

        while current_node is not None:
            if current_node.data == temp:
                if current_node.next is None:
                    current_node.prev.next = None
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next
                    current_node.next.prev = None
                break
            current_node = current_node.next

    # TAMPIL NODE
    def menuTampil(self):
        os.system('clear')
        print("Tampilkan list data:")
        current_node = self.head

        while current_node is not None:
            prev_data = current_node.prev.data if current_node.prev else None
            next_data = current_node.next.data if current_node.next else None
            
            print(prev_data, current_node.data, next_data)
            current_node = current_node.next

    # Display the program menu
    def menuUmum(self):
        pilih = "y"
        while pilih.lower() in ("y", "yes"):
            os.system('clear')
            print('Pilih menu yang anda inginkan')
            print('1: Tambah data ke linked list')
            print('2: Hapus data di linked list')
            print('3: Tampilkan data di linked list')
            print('4: Keluar Program')

            pilihan = input("Masukkan Menu yang anda pilih: ")

            if pilihan == "1":
                self.menuTambah()
            elif pilihan == "2":
                self.menuHapus()
            elif pilihan == "3":
                self.menuTampil()
            elif pilihan == "4":
                pilih = "n"
            else:
                pilih = "n" 

if __name__ == "__main__":
    # run
    d = DoubleList()
    d.menuUmum()
