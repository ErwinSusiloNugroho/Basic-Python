# 1. Memasukkan data makanan yang tidak disukai
makanan_tidak_disukai = []
jumlah_makanan_tidak_disukai = int(input("Berapa jenis makanan yang tidak kamu suka? "))

for i in range(jumlah_makanan_tidak_disukai):
    makanan = input("Masukkan makanan yang tidak kamu suka: ")
    makanan_tidak_disukai.append(makanan)

# 2. Memasukkan data makanan yang disukai
makanan_disukai = []
jumlah_makanan_disukai = int(input("Berapa jenis makanan yang kamu suka? "))

for i in range(jumlah_makanan_disukai):
    makanan = input("Masukkan makanan yang kamu suka: ")
    makanan_disukai.append(makanan)

# 3. Menampilkan masing-masing data pada list
print("\nMakanan yang tidak disukai:")
for makanan in makanan_tidak_disukai:
    print(makanan)

print("\nMakanan yang disukai:")
for makanan in makanan_disukai:
    print(makanan)

# 4. Menghapus salah satu makanan dari daftar makanan yang tidak disukai
makanan_hapus = input("\nMasukkan makanan yang ingin dihapus dari daftar tidak disukai: ")
if makanan_hapus in makanan_tidak_disukai:
    makanan_tidak_disukai.remove(makanan_hapus)
    print(f"{makanan_hapus} berhasil dihapus dari daftar tidak disukai.")
else:
    print(f"{makanan_hapus} tidak ditemukan dalam daftar tidak disukai.")

# 5. Menggabungkan list makanan yang disukai dan tidak disukai
makanan_gabungan = makanan_disukai + makanan_tidak_disukai

# Menampilkan hasil gabungan
print("\nGabungan Makanan:")
for makanan in makanan_gabungan:
    print(makanan)
