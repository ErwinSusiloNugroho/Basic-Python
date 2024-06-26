from collections import deque
import os

class Stack:
    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.popleft() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

    def size(self):
        return len(self.items)

    def mainmenu(self):
        pilih = "y"
        while pilih.lower() == "y":
            os.system("cls")  # Menggunakan "cls" untuk membersihkan layar di Windows
            print("| Menu aplikasi QUEUE |")
            print("------------------------")
            print("1. Tambah Data")
            print("2. Pop Objek")
            print("3. Cek Empty")
            print("4. Tampil objek terakhir")
            print("5. Panjang dari stack")
            print("6. Tampilkan semua data")
            print("------------------------")

            pilihan = input("Silakan masukkan pilihan anda: ")

            if pilihan == "1":
                obj = input("Masukkan objek yang ingin anda tambahkan: ")
                os.system("cls")
                print("Object " + obj + " telah ditambahkan")
                self.push(obj)
                input()
            elif pilihan == "2":
                os.system("cls")
                popped = self.pop()
                if popped is not None:
                    print("Objek " + str(popped) + " dihapus")
                else:
                    print("Stack kosong")
                input()
            elif pilihan == "3":
                os.system("cls")
                print(self.isEmpty())
                input()
            elif pilihan == "4":
                os.system("cls")
                top_item = self.peek()
                if top_item is not None:
                    print("Objek terakhir: " + str(top_item))
                else:
                    print("Stack kosong")
                input()
            elif pilihan == "5":
                os.system("cls")
                print("Panjang dari stack adalah: " + str(self.size()))
                input()
            elif pilihan == "6":
                os.system("cls")
                self.display_all()
                input()
            else:
                pilih = "n"

    def display_all(self):
        if self.isEmpty():
            print("Stack kosong")
        else:
            print("Isi stack:")
            for item in self.items:
                print(item)

if __name__ == "__main__":
    s = Stack()
    s.mainmenu()
    os.system("cls")
