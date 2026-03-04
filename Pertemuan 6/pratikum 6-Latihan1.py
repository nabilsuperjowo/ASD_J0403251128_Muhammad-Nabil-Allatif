#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1
        data[j + 1] = key
    return data

# Soal:
# 1. Mengapa perulangan dimulai dari indeks 1?
# 2. Apa fungsi variabel key?
# 3. Mengapa digunakan while, bukan for?
# 4. Operasi apa yang terjadi di dalam while?

# Jawab
# 1. karena index 0 berada di posisi sebagai tumpuan(sorted) awal.jadi perulangan di ambil dari index 1 untuk mengambil elemen ke 2
# 2. key disini berfungsi untuk menjadi penyimpanan sementara agar nilai sebelumnya tidak hilang
# 3. karena perulangan tidak tetap, jika menggunakan for kita harus menentukan mau berapa kali di ulang sedangkan menggunakan while kode akan berhenti jika semuanya sudah benar
# 4. terjadinya pergeseran nilai dari terbesar di geserkan ke kanan untuk membukakan ruang bagi key