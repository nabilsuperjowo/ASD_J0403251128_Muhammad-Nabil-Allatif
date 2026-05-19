def quick_sort(arr):
    """Sorts the list in place using the quick sort algorithm."""
    def _partition(a, low, high):
        """Partitions the array and returns the index of the pivot."""
        pivot = a[high]
        i = low - 1
        
        for j in range(low, high): # iterasi dari low ke high-1 untuk membandingkann setiap elemen dengan pivot
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i] # swap elemen yang lebih kecil atau sama dengan pivot ke posisi i
        a[i + 1], a[high] = a[high], a[i + 1] # swap pivot ke posisi yang benar (i + 1)
        
        return i + 1

    def _quick_sort(a, low, high):
        #
        if low < high:
            pi = _partition(a, low, high)
            _quick_sort(a, low, pi - 1)
            _quick_sort(a, pi + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)


if __name__ == "__main__": # contoh penggunaan 
    sample = [33, 10, 55, 71, 29, 18, 42] # sample dari contoh penggunaan quick sort
    print("Sebelum:", sample) # menampilkan list sebelum di urutkan
    quick_sort(sample) # memanggil fungsi quick_sort untuk mengurutkan list sample
    print("Sesudah:", sample) # menampilkan list setelah di urutkan
