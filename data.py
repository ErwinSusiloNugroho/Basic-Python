# Inisialisasi data barang dari CV Abadi dan CV Prima Jaya
data_barang = {
    'CV Abadi': [
        {'Nama_barang': 'Shampo Dove Botol 200ml', 'Jum_Stok': 24},
        {'Nama_barang': 'SoKlin Cair 750 ml (All variant)', 'Jum_Stok': 36},
        {'Nama_barang': 'Sabun mandi Livebuoy cair 750ml', 'Jum_Stok': 36},
        {'Nama_barang': 'Pepsodent 75gr', 'Jum_Stok': 36},
        {'Nama_barang': 'Rinso Anti Noda 1000gr', 'Jum_Stok': 24}
    ],
    'CV Prima Jaya': [
        {'Nama_barang': 'Gula Pasir (Gulaku) 1kg', 'Jum_Stok': 40},
        {'Nama_barang': 'Beras Wangi 5kg', 'Jum_Stok': 24},
        {'Nama_barang': 'Tepung Terigu 1kg', 'Jum_Stok': 24},
        {'Nama_barang': 'Minyak Goreng Tropical 2L', 'Jum_Stok': 24},
        {'Nama_barang': 'Telur Ayam Nutrisi Tinggi', 'Jum_Stok': 60}
    ]
}

# Input data transaksi pengiriman barang dari CV Anda sendiri
nama_cv = "CV PELANGI"
data_barang[nama_cv] = []

# Menginput jumlah barang dan detail barang yang dikirim dari CV Anda sendiri
tanggal_pengiriman = '20-11-2023'  
print(f"Masukkan data transaksi pengiriman barang dari {nama_cv} pada tanggal {tanggal_pengiriman}:")
jumlah_barang_anda = int(input("Masukkan jumlah barang yang akan dikirim: "))
for i in range(jumlah_barang_anda):
    nama_barang = input(f"Masukkan nama barang ke-{i+1}: ")
    jumlah_stok = int(input(f"Masukkan jumlah stok barang {nama_barang}: "))
    data_barang[nama_cv].append({'Nama_barang': nama_barang, 'Jum_Stok': jumlah_stok, 'Tgl_kirim': tanggal_pengiriman})

# Menampilkan data barang dari CV Abadi
print("\nData Barang dari CV Abadi:")
for barang in data_barang['CV Abadi']:
    print(f"Nama Barang: {barang['Nama_barang']}")
    print(f"Jum_Stok: {barang['Jum_Stok']}")
    print()

# Menampilkan data barang dari CV Prima Jaya
print("Data Barang dari CV Prima Jaya:")
for barang in data_barang['CV Prima Jaya']:
    print(f"Nama Barang: {barang['Nama_barang']}")
    print(f"Jum_Stok: {barang['Jum_Stok']}")
    print()

# Menampilkan data barang dari CV Anda sendiri
print(f"Data Barang dari {nama_cv}:")
for barang in data_barang[nama_cv]:
    print(f"Nama Barang: {barang['Nama_barang']}")
    print(f"Jum_Stok: {barang['Jum_Stok']}")
    print(f"Tgl_kirim: {barang['Tgl_kirim']}")
   
print("\nEstimasi kedatangan 3 hari dari pre-order\nTerimakasih telah mempercayai cv kami")