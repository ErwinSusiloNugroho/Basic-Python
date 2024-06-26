class Antrian:
    def __init__(self):
        self.daftar_antrian = []

    def masukkan_antrian(self, data):
        self.daftar_antrian.append(data)

    def ambil_antrian(self):
        if not self.kosong():
            return self.daftar_antrian.pop(0)
        else:
            print("Antrian kosong.")

    def kosong(self):
        return len(self.daftar_antrian) == 0

    def ukuran(self):
        return len(self.daftar_antrian)

    def depan(self):
        if not self.kosong():
            return self.daftar_antrian[0]
        else:
            print("Antrian kosong.")

# Contoh penggunaan:
antrian_saya = Antrian()

antrian_saya.masukkan_antrian(1)
antrian_saya.masukkan_antrian(2)
antrian_saya.masukkan_antrian(3)

print("Depan antrian:", antrian_saya.depan())
print("Ukuran antrian:", antrian_saya.ukuran())

item_dihapus = antrian_saya.ambil_antrian()
print("Item yang diambil dari antrian:", item_dihapus)

print("Ukuran antrian yang diperbarui:", antrian_saya.ukuran())
