print("Program Menghitung Total Pembeliaan")

print("Selamat Datang Di IndoApril Universitas April")
#Menginput Login Member
print = input("Masukkan No Member : ")
print = input("Masukkan Nama : ")
print = input("Masukkan NIM : ")
print = input("Masukkan Program Studi : ")
print = input("Masukkan Kelas : ")

#menghitung total harga barang berdasarkan harga barang dan jumlah pembelian 

#Menginput harga barang dan jumlah pembelian
harga =int(input("Masukkan harga barang: Rp. "))
jumlah = float(input("Masukkan jumlahh pembelian: "))

#Mengitung total harga barang
total_harga = harga * jumlah

#Menampilkan hasil harga
print = input(total_harga)

#Menghitung diskon 25%, jika pembelian > 250.000
if total_harga > 250000:
    diskon = total_harga * 0.25
    total_harga -= diskon
    print = input ("total harga barang: Rp." + str(total_harga)+ " (diskon 25%: Rp. "+ str(diskon)+")")
else:
    print = input("total harga barang: Rp." + str(total_harga))

#Menanyakan apakah ingin menghitung ulang
while True:
    pilihan = input("Apa ingin menghitung total harga kembali? (y/t): ")
    if pilihan != 'y':
        print = input("Terima kasih telah berbelanja di sini")
        break
