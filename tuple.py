# Membuat tuple untuk menghitung nilai akhir mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
nilai_mahasiswa = []

for i in range(jumlah_mahasiswa):
    nama = input(f"Masukkan nama mahasiswa {i + 1}: ")
    nilai1 = float(input("Masukkan nilai 1: "))
    nilai2 = float(input("Masukkan nilai 2: "))
    nilai3 = float(input("Masukkan nilai 3: "))
    nilai_mahasiswa.append((nama, nilai1, nilai2, nilai3))

# Menghitung nilai akhir untuk setiap mahasiswa
nilai_akhir = [(nama, (nilai1 + nilai2 + nilai3) / 3) for nama, nilai1, nilai2, nilai3 in nilai_mahasiswa]

# Menampilkan nilai minimal dan maksimal
nilai_minimal = min(nilai_akhir, key=lambda x: x[1])
nilai_maksimal = max(nilai_akhir, key=lambda x: x[1])

print("\nNilai Akhir Mahasiswa:")
for nama, nilai in nilai_akhir:
    print(f"{nama}: {nilai:.2f}")

print("\nNilai Minimal:")
print(f"{nilai_minimal[0]}: {nilai_minimal[1]:.2f}")

print("\nNilai Maksimal:")
print(f"{nilai_maksimal[0]}: {nilai_maksimal[1]:.2f}")
