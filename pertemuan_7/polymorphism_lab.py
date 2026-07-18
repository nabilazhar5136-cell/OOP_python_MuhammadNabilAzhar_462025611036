class AlatPembayaran:
    def proses_bayar(self, jumlah):
        print(f"Memproses pembayaran sebesar Rp{jumlah}")


class KartuKredit(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} berhasil menggunakan Kartu Kredit")


class EWallet(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} berhasil menggunakan E-Wallet")


class TransferBank:
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah} berhasil menggunakan Transfer Bank")


def jalankan_transaksi(objek, jumlah):
    objek.proses_bayar(jumlah)


kartu_kredit = KartuKredit()
e_wallet = EWallet()
transfer_bank = TransferBank()

jalankan_transaksi(kartu_kredit, 50000)
jalankan_transaksi(e_wallet, 75000)
jalankan_transaksi(transfer_bank, 100000)
