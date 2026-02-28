#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Latihan 3 : Rekursi pada List
#=======================================================================================================

def cari_maks(data, index=0):
    # base case : jika di elemen terakhir
    if index == len(data) - 1:
        return data[index]
    
    # recursive case : cari maksimum sisa list
    maks_sisa = cari_maks(data, index + 1)
    
    # bandingkan elemen sekarang dengan sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

print("=======Program Cari Nilai Maksimum=======")
angka = [3, 7, 2, 9, 5]
print(cari_maks(angka))