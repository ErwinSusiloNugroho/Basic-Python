# 1. Buat list untuk makanan yang tidak disukai
makanan_tidak_suka = []
jumlah_makanan_tidak_suka = int(input("Masukkan jumlah makanan yang tidak kamu suka: "))
for i in range(jumlah_makanan_tidak_suka):
    makanan_tidak_suka.append(input(f"Masukkan makanan yang tidak kamu suka ke-{i + 1}: "))

# 2. Buat list untuk makanan yang disukai
makanan_suka = []
jumlah_makanan_suka = int(input("Masukkan jumlah makanan yang kamu suka: "))
for i in range(jumlah_makanan_suka):
    makanan_suka.append(input(f"Masukkan makanan yang kamu suka ke-{i + 1}: "))

# 3. Tampilkan masing-masing data pada list
print("\nMakanan yang tidak disukai:")
for makanan in makanan_tidak_suka:
    print(makanan)

print("\nMakanan yang disukai:")
for makanan in makanan_suka:
    print(makanan)

# 4. Hapus salah satu makanan dari daftar yang tidak disukai
makanan_yang_dihapus = input("\nMasukkan makanan yang akan dihapus dari daftar yang tidak disukai: ")
if makanan_yang_dihapus in makanan_tidak_suka:
    makanan_tidak_suka.remove(makanan_yang_dihapus)
    print(f"{makanan_yang_dihapus} berhasil dihapus dari daftar yang tidak disukai.")
else:
    print(f"{makanan_yang_dihapus} tidak ditemukan dalam daftar yang tidak disukai.")

# 5. Gabungkan list makanan yang suka dan tidak suka
makanan_gabungan = makanan_suka + makanan_tidak_suka
print("\nGabungan makanan yang suka dan tidak suka:")
for makanan in makanan_gabungan:
    print(makanan)
