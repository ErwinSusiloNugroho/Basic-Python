import os

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

    def size(self):
        return len(self.items)

    def mainmenu(self):
        pilih = "y"
        while pilih.lower() == "y":
            os.system("clear")
            print("| Menu aplikasi stack |")
            print("------------------------")
            print("1. Push objek")
            print("2. Pop objek")
            print("3. Cek Empty")
            print("4. Tampil objek terakhir")
            print("5. Panjang dari stack")
            print("------------------------")

            pilihan = input("Silakan masukkan pilihan anda: ")

            if pilihan == "1":
                obj = input("Masukkan objek yang ingin anda tambahkan: ")
                os.system("clear")
                print("Object " + obj + " telah ditambahkan")
                self.push(obj)
                input()
            elif pilihan == "2":
                os.system("clear")
                popped = self.pop()
                if popped is not None:
                    print("Objek " + str(popped) + " dihapus")
                else:
                    print("Stack kosong")
                input()
            elif pilihan == "3":
                os.system("clear")
                print(self.isEmpty())
                input()
            elif pilihan == "4":
                os.system("clear")
                top_item = self.peek()
                if top_item is not None:
                    print("Objek terakhir: " + str(top_item))
                else:
                    print("Stack kosong")
                input()
            elif pilihan == "5":
                os.system("clear")
                print("Panjang dari stack adalah: " + str(self.size()))
                input()
            else:
                pilih = "n"

if __name__ == "__main__":
    s = Stack()
    s.mainmenu()
    os.system("clear")
