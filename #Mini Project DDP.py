#Menginput Biodata
Nama = "Khairunisa Aprilia"
NIM = "2409116060"
Kelas = "B"

#Menampilkan Biodata
print(Nama)
print(NIM)
print(Kelas)

#menghitung total harga barang berdasarkan harga barang dan jumlah pembelian 

#Menginput harga barang dan jumlah pembelian
harga =int(input("masukkan harga barang: Rp. "))
jumlah = float(input("masukkan jumlahh pembelian: "))

#Mengitung total harga barang
total_harga = harga * jumlah

#Menampilkan hasil harga
print(total_harga)

#Menghitung diskon 25%, jika pembelian > 250.000
if total_harga > 250000:
    diskon = total_harga * 0.25
    total_harga -= diskon
    print("total harga barang: Rp." + str(total_harga)+ " (diskon 25%: Rp. "+ str(diskon)+")")
else:
    print("total harga barang: Rp." + str(total_harga))

#Menanyakan apakah ingin menghitung ulang
while True:
    pilihan = input("Apa ingin menghitung total harga kembali? (y/t): ")
    if pilihan != 'y':
        print("Terima kasih telah berbelanja di sini")
        break
