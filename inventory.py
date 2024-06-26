class InventorySystem:
    def __init__(self):
        self.data = []

    def tambah_data(self, no, tgl_kirim, nama_supplier, detail_barang):
        entry = {
            'No': no,
            'Tgl_kirim': tgl_kirim,
            'Nama_supplier': nama_supplier,
            'Detail_barang': detail_barang
        }
        self.data.append(entry)
        print("Data berhasil ditambahkan.")

    def tampilkan_data(self):
        if not self.data:
            print("Data kosong.")
        else:
            print("Data Inventori:")
            for entry in self.data:
                print(f"\nNo: {entry['No']}, Tgl_kirim: {entry['Tgl_kirim']}, Nama_supplier: {entry['Nama_supplier']}")
                print("Detail Barang:")
                for barang in entry['Detail_barang']:
                    print(f"  - Nama_barang: {barang['Nama_barang']}, Jum_Stok: {barang['Jum_Stok']}")

# Membuat objek InventorySystem
inventori = InventorySystem()

# Meminta input dari pengguna untuk informasi utama
brp = int(input("Masukkan jumlah nomor: "))
for i in range(brp):
    no = int(input("Masukkan Nomor: "))
    tgl_kirim = input("Masukkan Tanggal Kirim: ")

    # Meminta input dari pengguna untuk supplier dan barang
    nama_supplier = input("Masukkan Nama Supplier: ")

    detail_barang = []
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    for j in range(jumlah_barang):
        nama_barang = input(f"Masukkan Nama Barang ke-{j + 1}: ")
        jum_stok = int(input(f"Masukkan Jumlah Stok Barang ke-{j + 1}: "))
        detail_barang.append({'Nama_barang': nama_barang, 'Jum_Stok': jum_stok})

    # Menambahkan data ke dalam list (dalam loop)
    inventori.tambah_data(no, tgl_kirim, nama_supplier, detail_barang)

# Menampilkan data (di luar loop)
inventori.tampilkan_data()
