from collections import deque
import os
class queue:
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
            print("1. tambah data")
            print("2. Pop data")
            print("3. Cek Empty")
            print("4. Tampil objek terakhir")
            print("5. Panjang dari queue")
            print("6. Tampilkan semua data")
            print("7. keluar")
            print("------------------------")
            pilihan = input("Silakan masukkan pilihan anda: ")
            if pilihan == "1":
                obj = input("Masukkan data yang ingin anda tambahkan: ")
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
                    print("Data kosong")
                input()
            elif pilihan == "3":
                os.system("cls")
                print(self.isEmpty())
                input()
            elif pilihan == "4":
                os.system("cls")
                top_item = self.peek()
                if top_item is not None:
                    print("data terakhir: " + str(top_item))
                else:
                    print("data kosong")
                input()
            elif pilihan == "5":
                os.system("cls")
                print("Panjang data adalah: " + str(self.size()))
                input()
            elif pilihan == "6":
                os.system("cls")
                self.display_all()
                input()
            elif pilihan == "7":
                os.system("cls")
                exit() 

            else:
                pilih = "n"
    def display_all(self):
        if self.isEmpty():
            print("Data kosong")
        else:
            print("Isi data:")
            for item in self.items:
                print(item)
if __name__ == "__main__":
    s = queue()
    s.mainmenu()
    os.system("cls")