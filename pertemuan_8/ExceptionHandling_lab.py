class SaldoTidakCukupError(Exception):
    pass


class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    # Method untuk melakukan penarikan
    def tarik_uang(self, jumlah):
        if jumlah > self.saldo:
            raise SaldoTidakCukupError(
                "Penarikan gagal! Saldo tidak mencukupi."
            )

        self.saldo -= jumlah
        print(f"Penarikan sebesar Rp{jumlah} berhasil.")
        print(f"Sisa saldo: Rp{self.saldo}")


rekening = RekeningBank("Nabil", 500000)

try:
    print(f"Nama Nasabah: {rekening.nama}")
    print(f"Saldo Awal: Rp{rekening.saldo}")

    rekening.tarik_uang(700000)

except SaldoTidakCukupError as error:
    print(f"Terjadi kesalahan: {error}")

finally:
    print("Proses pemeriksaan transaksi telah selesai dilakukan.")

