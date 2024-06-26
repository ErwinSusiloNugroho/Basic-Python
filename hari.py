hari = {1: 'senin', 2: 'selasa', 3: 'rabu', 4: 'kamis', 5: 'jumat', 6: 'sabtu', 7: 'minggu'}

dino = input("Masukkan hari: ")
angka = int(input("Masukkan angka: "))

# Mengubah nama hari menjadi lowercase dan menghitung indeks
indeks_hari = (list(hari.values()).index(dino.lower()) + angka ) % 7 

# Mendapatkan hari hasil
hasil_hari = list(hari.values())[indeks_hari]

print(f"Hasil: {hasil_hari}")
