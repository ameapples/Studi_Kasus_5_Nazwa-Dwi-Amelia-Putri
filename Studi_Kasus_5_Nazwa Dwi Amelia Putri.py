# Sistem Perhitungan Biaya Parkir

# Function untuk menghitung biaya parkir
def hitung_biaya_parkir(jenis_kendaraan, durasi):

# Parameter jenis kendaraan dan durasi parkir serta cabang untuk menentukan tarif
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000
    else:
        return 0

# Hitung biaya berdasarkan lama durasi parkir
    total_biaya = tarif * durasi

# Mengembalikan total biaya
    return total_biaya

# Input data kendaraan
jenis_kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ").lower()
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

# Hitung lama parkir
lama_parkir = jam_keluar - jam_masuk

# Memanggil function
total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

# Hasil/output
print("\n=== HASIL PERHITUNGAN PARKIR ===")
print("Jenis kendaraan :", jenis_kendaraan)
print("Jam masuk       :", jam_masuk)
print("Jam keluar      :", jam_keluar)
print("Lama parkir     :", lama_parkir, "jam")
print("Total biaya     : Rp", total_biaya)
print("Terima kasih :D")