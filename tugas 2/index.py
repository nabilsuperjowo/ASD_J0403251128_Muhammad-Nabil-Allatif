# Nama file tempat menyimpan data stok barang
NAMA_FILE = "StockBarang.txt"


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):

    # Dictionary untuk menyimpan data barang
    stok_dict = {}

    try:
        # Membuka file dalam mode baca
        with open(nama_file, "r", encoding="utf-8") as f:

            # Membaca setiap baris dalam file
            for baris in f:

                # Menghapus spasi dan newline di akhir baris
                baris = baris.strip()

                # Jika baris kosong → lewati
                if not baris:
                    continue

                # Memisahkan data berdasarkan koma
                parts = baris.split(",")

                # Validasi jumlah kolom harus 3
                if len(parts) != 3:
                    continue

                # Simpan ke variabel
                kode, nama, stok_str = parts

                # Simpan ke dictionary dengan stok sebagai integer
                stok_dict[kode] = {
                    "nama": nama,
                    "stok": int(stok_str)
                }

    # Jika file belum ada
    except FileNotFoundError:
        print("File belum ditemukan. Membuat data baru...")

    # Mengembalikan dictionary stok
    return stok_dict


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):

    # Membuka file dalam mode tulis (overwrite)
    with open(nama_file, "w", encoding="utf-8") as f:

        # Menulis data berdasarkan urutan kode
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]

            # Menulis ke file dengan format CSV
            f.write(f"{kode},{nama},{stok}\n")


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):

    # Jika data kosong
    if not stok_dict:
        print("Stok kosong.")
        return

    # Header tabel
    print("\nKode       | Nama Barang     | Stok")
    print("-" * 36)

    # Menampilkan semua barang
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]

        # Cetak dalam format rapi
        print(f"{kode:<10} | {nama:<15} | {stok:>4}")


# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):

    # Input kode barang dari user
    kode = input("Masukkan kode barang: ").strip()

    # Jika kode ditemukan
    if kode in stok_dict:
        data = stok_dict[kode]

        print("\nBarang ditemukan:")
        print(f"Kode : {kode}")
        print(f"Nama : {data['nama']}")
        print(f"Stok : {data['stok']}")

    # Jika tidak ditemukan
    else:
        print("Barang tidak ditemukan.")


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):

    # Input kode baru
    kode = input("Masukkan kode barang baru: ").strip()

    # Validasi kode tidak boleh duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    # Input nama barang
    nama = input("Masukkan nama barang: ").strip()

    # Input stok awal dengan validasi angka
    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus angka.")
        return

    # Validasi stok tidak boleh negatif
    if stok_awal < 0:
        print("Stok tidak boleh negatif.")
        return

    # Simpan barang ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan.")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):

    # Input kode barang
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # Validasi kode harus ada
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    # Menu jenis update
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    # Input jumlah perubahan
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus angka.")
        return

    # Stok saat ini
    stok_sekarang = stok_dict[kode]["stok"]

    # Tambah stok
    if pilihan == "1":
        stok_dict[kode]["stok"] = stok_sekarang + jumlah
        print("Stok berhasil ditambahkan.")

    # Kurangi stok
    elif pilihan == "2":

        # Cek agar stok tidak negatif
        if stok_sekarang - jumlah < 0:
            print("Error: stok tidak boleh negatif.")
            return

        stok_dict[kode]["stok"] = stok_sekarang - jumlah
        print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid.")


# -------------------------------
# Program Utama
# -------------------------------
def main():

    # Membaca data dari file saat program dimulai
    StockBarag = baca_stok(NAMA_FILE)

    # Loop menu utama
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        # Menjalankan fungsi sesuai pilihan
        if pilihan == "1":
            tampilkan_semua(StockBarag)

        elif pilihan == "2":
            cari_barang(StockBarag)

        elif pilihan == "3":
            tambah_barang(StockBarag)

        elif pilihan == "4":
            update_stok(StockBarag)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, StockBarag)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program utama jika file dijalankan langsung
if __name__ == "__main__":
    main()