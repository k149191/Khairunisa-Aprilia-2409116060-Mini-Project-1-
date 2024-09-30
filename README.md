![mini project drawio](https://github.com/user-attachments/assets/326707e8-3004-4aab-bd91-5df310849afd)

PENJELASAN = Baris 1 sebagai judul program
print("Program Menghitung Total Pembeliaan")
PENJELASAN = Baris 3-13 Melakukan Login Member 
#Menginput Login Member 
Member = "IndoApril"
Nama = "Khairunisa Aprilia"
NIM = "2409116060"
Kelas = "B"

#Menampilkan Login Member
print(Member)
print(Nama)
print(NIM)
print(Kelas)
PENJELASAN = BARIS 15-25 Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian 
#menghitung total harga barang berdasarkan harga barang dan jumlah pembelian 

#Menginput harga barang dan jumlah pembelian
harga =int(input("masukkan harga barang: Rp. "))
jumlah = float(input("masukkan jumlahh pembelian: "))

#Mengitung total harga barang
total_harga = harga * jumlah

#Menampilkan hasil harga
print(total_harga)
PENJELASAN = Baris 27-33 menghitung diskon.  Jika lebih dari Rp. 250.000, tambahkan diskon sebesar 25%. Sedangkan jika tidak mencapai lebih dari Rp.250.000, maka tidak mendapatkan diskon
#Menghitung diskon 25%, jika pembelian > 250.000
if total_harga > 250000:
    diskon = total_harga * 0.25
    total_harga -= diskon
    print("total harga barang: Rp." + str(total_harga)+ " (diskon 25%: Rp. "+ str(diskon)+")")
else:
    print("total harga barang: Rp." + str(total_harga))
PENJELASAN = Baris 35-40 menanyakan apakah ingin menghitung ulang total harga pembelian kembari atau tidak
#Menanyakan apakah ingin menghitung ulang
while True:
    pilihan = input("Apa ingin menghitung total harga pembelian kembali? (y/t): ")
    if pilihan != 'y':
        print("Terima kasih telah berbelanja di sini")
        break



![Screenshot 2024-10-01 061537](https://github.com/user-attachments/assets/fe04e78f-2095-428c-a7b3-d7eaf31a554a)


![Screenshot 2024-10-01 061820](https://github.com/user-attachments/assets/1cf5f95b-af35-4f72-b579-002b7bc217cf)



  
