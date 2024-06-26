data_barang = {
    'CV Abadi': [
        {'No': 1, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Shampo Dove Botol 200ml', 'Jum_Stok': 24},
        {'No': 2, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'SoKlin Cair 750 ml (All variant)', 'Jum_Stok': 36},
        {'No': 3, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Sabun mandi Livebuoy cair 750ml', 'Jum_Stok': 36},
        {'No': 4, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Pepsodent 75gr', 'Jum_Stok': 36},
        {'No': 5, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Rinso Anti Noda 1000gr', 'Jum_Stok': 24}
    ],
    'CV Prima Jaya': [
        {'No': 1, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Gula Pasir (Gulaku) 1kg', 'Jum_Stok': 40},
        {'No': 2, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Beras Wangi 5kg', 'Jum_Stok': 24},
        {'No': 3, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Tepung Terigu 1kg', 'Jum_Stok': 24},
        {'No': 4, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Minyak Goreng Tropical 2L', 'Jum_Stok': 24},
        {'No': 5, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Telur Ayam Nutrisi Tinggi', 'Jum_Stok': 60}
    ]
}

# Tampung data jumlah stok dari kedua CV
stok_abadi = {barang['Nama_barang']: barang['Jum_Stok'] for barang in data_barang['CV Abadi']}
stok_prima = {barang['Nama_barang']: barang['Jum_Stok'] for barang in data_barang['CV Prima Jaya']}

# Identifikasi data jumlah stok yang tidak sama antara CV Abadi dan CV Prima Jaya
beda_stok = {barang for barang in stok_abadi if stok_abadi[barang] != stok_prima.get(barang)}

data_barang = {
    'CV Abadi': [
        {'No': 1, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Shampo Dove Botol 200ml', 'Jum_Stok': 24},
        {'No': 2, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'SoKlin Cair 750 ml (All variant)', 'Jum_Stok': 36},
        {'No': 3, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Sabun mandi Livebuoy cair 750ml', 'Jum_Stok': 36},
        {'No': 4, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Pepsodent 75gr', 'Jum_Stok': 36},
        {'No': 5, 'Tgl_kirim': '2-11-2023', 'Nama_supplier': 'CV Abadi', 'Nama_barang': 'Rinso Anti Noda 1000gr', 'Jum_Stok': 24}
    ],
    'CV Prima Jaya': [
        {'No': 1, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Gula Pasir (Gulaku) 1kg', 'Jum_Stok': 40},
        {'No': 2, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Beras Wangi 5kg', 'Jum_Stok': 24},
        {'No': 3, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Tepung Terigu 1kg', 'Jum_Stok': 24},
        {'No': 4, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Minyak Goreng Tropical 2L', 'Jum_Stok': 24},
        {'No': 5, 'Tgl_kirim': '11-11-2023', 'Nama_supplier': 'CV Prima Jaya', 'Nama_barang': 'Telur Ayam Nutrisi Tinggi', 'Jum_Stok': 60}
    ]
}

# Tampung data jumlah stok dari kedua CV
stok_abadi = {barang['Nama_barang']: barang['Jum_Stok'] for barang in data_barang['CV Abadi']}
stok_prima = {barang['Nama_barang']: barang['Jum_Stok'] for barang in data_barang['CV Prima Jaya']}

# Identifikasi data jumlah stok yang tidak sama antara CV Abadi dan CV Prima Jaya
beda_stok = {barang for barang in stok_abadi if stok_abadi[barang] != stok_prima.get(barang)}

# Menampilkan data barang dari CV Abadi
print("Data Barang dari CV Abadi:")
for barang in data_barang['CV Abadi']:
    print(f"No: {barang['No']}, Tgl_kirim: {barang['Tgl_kirim']}, Nama_supplier: {barang['Nama_supplier']}, Nama_Barang: {barang['Nama_barang']}, Jum_Stok: {barang['Jum_Stok']}")
    print()
    
# Menampilkan data barang dari CV Prima Jaya
print("Data Barang dari CV Prima Jaya:")
for barang in data_barang['CV Prima Jaya']:
    print(f"No: {barang['No']}, Tgl_kirim: {barang['Tgl_kirim']}, Nama_supplier: {barang['Nama_supplier']}, Nama_Barang: {barang['Nama_barang']}, Jum_Stok: {barang['Jum_Stok']}")
    print()

# Menampilkan hasil identifikasi data jumlah stok yang tidak sama
if beda_stok:
    print("Data jumlah stok yang tidak sama antara CV Abadi dan CV Prima Jaya:")
    for barang in beda_stok:
        print(f"Nama Barang: {barang}")
else:
    print("Tidak ada perbedaan jumlah stok antara CV Abadi dan CV Prima Jaya.")    