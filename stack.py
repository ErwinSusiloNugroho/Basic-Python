class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.is_full():
            print("Stack penuh, tidak dapat menambahkan data.")
        else:
            self.stack.append(data)
            self.top += 1
            print(f"{data} ditambahkan ke dalam stack.")

    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak dapat menghapus data.")
            return None
        else:
            item = self.stack.pop()
            self.top -= 1
            print(f"{item} dihapus dari stack.")
            return item

    def display(self):
        if self.is_empty():
            print("Stack kosong.")
        else:
            print("Isi Stack:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

# Inisialisasi stack dengan ukuran 5
stack_size = 5
stack = Stack(stack_size)

# Menambahkan data ke dalam stack
data = ["Buku", "Majalah", "Koran", "Kertas", "Mika"]
for item in data:
    stack.push(item)

# Menampilkan isi stack
stack.display()

# Menghapus data dari stack
stack.pop()
stack.pop()

# Menampilkan isi stack setelah penghapusan
stack.display()
