hari = {
  1: 'senin',
  2: 'selasa',
  3: 'rabu',
  4: 'kamis',
  5: 'jumat',
  6: 'sabtu',
  7: 'minggu'
}

dino = input("Masukan hari: ").lower()
angka = int(input("Masukan angka: "))

if dino in hari.values():
    indeks_hari = (list(hari.values()).index(dino) + angka) % 7
    hasil_hari = list(hari.values())[indeks_hari]
    print(f"harinya: {hasil_hari}")
elif dino & angka == '':
     print("masukan data yang benar!") 
else:
    print("masukan data yang benar!")
