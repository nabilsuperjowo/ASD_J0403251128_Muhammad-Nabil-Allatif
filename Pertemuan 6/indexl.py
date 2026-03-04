a = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

# sorted(a) mengembalikan list baru yang urut
print("Hasil sorted(a):", sorted(a)) 

# Cek list asli, urutannya masih tetap seperti semula
print("List asli setelah sorted:", a)


a = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

# a.sort() mengurutkan list di tempat (in-place)
a.sort()

# Sekarang, variabel 'a' sudah berubah menjadi urut
print("List asli setelah a.sort():", a)