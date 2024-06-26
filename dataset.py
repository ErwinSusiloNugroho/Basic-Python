# Data set untuk CV Abadi
cv_abadi_data = {
    "Shampo Dove Botol 200ml": 24,
    "SoKlin Cair 750 ml (All variant)": 36,
    "Sabun mandi Livebuoy cair 750ml": 36,
    "Pepsodent 75gr": 36,
    "Rinso Anti Noda 1000gr": 24,
}

# Data set untuk CV Prima Jaya
cv_prima_jaya_data = {
    "Gula Pasir (Gulaku) 1kg": 40,
    "Beras Wangi 5kg": 24,
    "Tepung Terigu 1kg": 24,
    "Minyak Goreng Tropical 2L": 24,
    "Telur Ayam Nutrisi Tinggi": 60,
}


nilai_stok_sama = set(cv_abadi_data.values()) & set(cv_prima_jaya_data.values())

if nilai_stok_sama:
    print("Nilai stok yang sama antara kedua CV adalah:")
    print(nilai_stok_sama)
else:
    print("Tidak ada nilai stok yang sama antara kedua CV.")
