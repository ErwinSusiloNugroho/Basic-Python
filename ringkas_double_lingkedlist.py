import os 

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data, self.prev, self.next = data, prev, next

class DoubleList:
    def __init__(self):
        self.head = self.tail = None    

    def menuTambah(self):
        self.clear_screen()
        try:
            temp = int(input('Masukkan data baru = '))
        except ValueError:
            print("Input harus berupa angka.")
            input("Tekan Enter untuk melanjutkan...")
            return

        new_node = Node(temp, self.tail)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node

    def menuHapus(self):
        self.clear_screen()
        try:
            temp = int(input('Masukkan data yang akan dihapus = '))
        except ValueError:
            print("Input harus berupa angka.")
            input("Tekan Enter untuk melanjutkan...")
            return

        current_node = self.head
        while current_node:
            if current_node.data == temp:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev

                break

            current_node = current_node.next

    def menuTampil(self):
        self.clear_screen()
        print("Tampilkan list data:")
        current_node = self.head

        while current_node:
            prev_data = current_node.prev.data if current_node.prev else None
            next_data = current_node.next.data if current_node.next else None
            
            print(prev_data, current_node.data, next_data)
            current_node = current_node.next

        input("Tekan Enter untuk melanjutkan...")

    def menuUmum(self):
        while True:
            self.clear_screen()
            print('Pilih menu yang Anda inginkan\n1: Tambah data\n2: Hapus data\n3: Tampilkan data\n4: Keluar Program')
            pilihan = input("Masukkan Menu yang Anda pilih: ")

            if pilihan == "1":
                self.menuTambah()
            elif pilihan == "2":
                self.menuHapus()
            elif pilihan == "3":
                self.menuTampil()
            elif pilihan == "4":
                break
            else:
                input("Menu tidak valid. Tekan Enter untuk melanjutkan...")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    d = DoubleList()
    d.menuUmum()
