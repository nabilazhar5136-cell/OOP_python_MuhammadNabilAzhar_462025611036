class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan


mahasiswa1 = Mahasiswa("Andi Saputra", "241001", "Teknik Informatika")
mahasiswa2 = Mahasiswa("Budi Santoso", "241002", "Sistem Informasi")

print(f"Mahasiswa 1 -> Nama: {mahasiswa1.nama}, NIM: {mahasiswa1.nim}, Jurusan: {mahasiswa1.jurusan}")
print(f"Mahasiswa 2 -> Nama: {mahasiswa2.nama}, NIM: {mahasiswa2.nim}, Jurusan: {mahasiswa2.jurusan}")