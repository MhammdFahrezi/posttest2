from prettytable import PrettyTable

penjual = {"nama_penjual": "ziy", "sandi_penjual": "12345"}
pembeli = {"nama_pelanggan": "konsumen", "sandi_pelanggan": "54321"}

def login():
    nama = input("Masukkan nama: ")
    sandi = input("Masukkan sandi: ")
    if (nama, sandi) == (penjual["nama_penjual"], penjual["sandi_penjual"]):
        print("Login penjual berhasil")
        menu_penjual()
    elif (nama, sandi) == (pembeli["nama_pelanggan"], pembeli["sandi_pelanggan"]):
        print("selamat_datang_di_toko_habsyi_hadroh")
        menu_pembeli()
    else:
        print("Ada yang salah, coba lagi.")
        login()

stok_toko = [
    {"no": 1, "nama_barang": "bass", "bayar_menggunakan": "transfer,COD", "jumlah_barang": 5, "harga_barang": 120000},
    {"no": 2, "nama_barang": "stik_bass", "bayar_menggunakan": "transfer,COD", "jumlah_barang": 10, "harga_barang": 20000},
    {"no": 3, "nama_barang": "tam_mika", "bayar_menggunakan": "transfer,COD", "jumlah_barang": 15, "harga_barang": 250000},
    {"no": 4, "nama_barang": "darbuka", "bayar_menggunakan": "transfer,COD", "jumlah_barang": 20, "harga_barang": 225000},
    {"no": 5, "nama_barang": "rebana", "bayar_menggunakan": "transfer,COD", "jumlah_barang": 25, "harga_barang": 300000},
]

def menu_penjual():
    while True:
        print("\nMenu Penjual:")
        print("1. Tambah barang")
        print("2. Lihat stok")
        print("3. Perbarui barang")
        print("4. Hapus barang")
        print("5. Keluar")
        
        menu = input("Pilih tindakan (1,2,3,4,5): ")
        
        if menu == "1":
            nama_barang = input("Masukkan nama barang: ")
            harga_barang = float(input("Masukkan harga barang: "))
            jumlah_barang = int(input("Masukkan jumlah barang: "))
            stok_toko.append({"no": len(stok_toko) + 1, "nama_barang": nama_barang, "harga_barang": harga_barang, "jumlah_barang": jumlah_barang})
            print(f"{nama_barang} telah ditambahkan ke stok toko.")
        elif menu == "2":
            print("\nDaftar stok barang:")
            table = PrettyTable()
            table.field_names = ["No.", "Nama Barang", "Harga Barang", "Jumlah Barang"]
            for item in stok_toko:
                table.add_row([item["no"], item["nama_barang"], f"Rp{item['harga_barang']}", item["jumlah_barang"]])
            print(table)
        elif menu == "3":
            nama_barang = input("Masukkan nama barang yang akan diperbarui: ")
            found = False
            for item in stok_toko:
                if item["nama_barang"].lower() == nama_barang.lower():
                    found = True
                    new_price = float(input(f"Masukkan harga baru untuk {nama_barang}: "))
                    item["harga_barang"] = new_price
                    print(f"{nama_barang} telah diperbarui dengan harga baru Rp{new_price}")
                    break
            if not found:
                print(f"{nama_barang} tidak ditemukan dalam stok toko.")
        elif menu == "4":
            nama_barang = input("Masukkan nama barang yang akan dihapus: ")
            found = False
            for item in stok_toko:
                if item["nama_barang"].lower() == nama_barang.lower():
                    found = True
                    stok_toko.remove(item)
                    print(f"{nama_barang} telah dihapus dari stok toko.")
                    break
            if not found:
                print(f"{nama_barang} tidak ditemukan dalam stok toko.")
        elif menu == "5":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def menu_pembeli():
    while True:
        print("\nMenu Pembeli:")
        print("1. Beli barang")
        print("2. Lihat stok")
        print("3. Keluar")
        
        menu = input("Pilih tindakan (1,2,3): ")
        
        if menu == "1":
            nama_barang = input("Masukkan nama barang yang ingin dibeli: ")
            found = False
            for item in stok_toko:
                if item["nama_barang"].lower() == nama_barang.lower():
                    found = True
                    if item["jumlah_barang"] > 0:
                        print(f"Anda telah membeli {nama_barang} dengan harga Rp{item['harga_barang']}")
                        item["jumlah_barang"] -= 1
                    else:
                        print(f"Maaf, stok {nama_barang} habis.")
                    break
            if not found:
                print(f"{nama_barang} tidak ditemukan dalam stok toko.")
        elif menu == "2":
            print("\nDaftar stok barang:")
            table = PrettyTable()
            table.field_names = ["No.", "Nama Barang", "Harga Barang", "Jumlah Barang"]
            for item in stok_toko:
                table.add_row([item["no"], item["nama_barang"], f"Rp{item['harga_barang']}", item["jumlah_barang"]])
            print(table)
        elif menu == "3":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    login()
