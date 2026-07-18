class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    # Menampilkan informasi objek
    def __str__(self):
        return f"Nama Produk: {self.nama}, Harga: Rp{self.harga}"

    # Sama dengan (==)
    def __eq__(self, produk_lain):
        return self.harga == produk_lain.harga

    # Lebih kecil (<)
    def __lt__(self, produk_lain):
        return self.harga < produk_lain.harga

    # Lebih besar (>)
    def __gt__(self, produk_lain):
        return self.harga > produk_lain.harga


# Membuat 3 object
produk1 = Produk("Buku", 10000)
produk2 = Produk("Pensil", 5000)
produk3 = Produk("Penggaris", 10000)

# Menguji __str__
print("=== Data Produk ===")
print(produk1)
print(produk2)
print(produk3)

# Menguji perbandingan
print("\n=== Hasil Perbandingan ===")
print(f"Apakah {produk1.nama} == {produk3.nama}? {produk1 == produk3}")
print(f"Apakah {produk1.nama} > {produk2.nama}? {produk1 > produk2}")
print(f"Apakah {produk2.nama} < {produk3.nama}? {produk2 < produk3}")