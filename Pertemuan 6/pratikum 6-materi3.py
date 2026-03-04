#=======================================================================================================
# Nama    : Muhammad Nabil Allatif
# NIM     : J0403251128
# Kelas   : TPL B2
#=======================================================================================================

#=======================================================================================================
# Merge sort(Ascending)
#=======================================================================================================

def merge_sort(data):
    
    if len(data) <= 1:
        return data

    #Divide membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slciing bagian kanan
    
    #recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted,right_sorted)

def merge(left, right):
    result = []
    i=0
    j=0
        
        #Membandingkan elemen kiri dan kanan 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
#menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
angka = [12,7,28,5,19,36,4]
print("hasil sorting merge sort", merge_sort(angka))

