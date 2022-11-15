print("----------------- SELAMAT DATANG DI REVITA COFFE SHOP -----------------")
nama = input("MASUKKAN NAMA ANDA : ")
Alamat = input("MASUKKAN ALAMAT ANDA : ")
No_telp = input("MASUKKAN NO_TELP : ")
Tanggal = input("MASUKKAN TANGGAL : ")




def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 12000")
   print("2. Mie Goreng - Rp 7000")
   print("3. Mie Rebus - Rp 7000")
   print("4. Roti Bakar Keju Susu - Rp 15000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*12000
       print (porsi," Porsi Nasi Goreng = Rp", totalmkn)
       mkn=("Roti Bakar")
   elif nomor==2:
       totalmkn=porsi*7000
       print (porsi," Porsi Mie Goreng = Rp", totalmkn)
       mkn=("Mie Goreng")
   elif nomor==3:
       totalmkn=porsi*7000
       print (porsi," Porsi Mie Rebus = Rp", totalmkn)
       mkn=("Mie Rebus")
   elif nomor==4:
       totalmkn=porsi*11000
       print (porsi, " Porsi Roti Bakar Keju Susu = Rp", totalmkn)
       mkn=("Roti Bakar Keju Susu")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es Teh Manis - Rp 5000")
   print("2. Es Jeruk - Rp 9000")
   print("3. Kopi - Rp 4000")
   print("4. Nutrisari - Rp 5000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*5000
       print (gelas," Es Teh Manis = Rp", totalmnm)
       mnm=(" Gelas Es Teh Manis")
   elif nomor==2:
       totalmnm=gelas*9000
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Kopi")
   elif nomor==4:
       totalmnm=gelas*5000
       print (gelas, " Gelas Nutrisari = Rp", totalmnm)
       mnm=("Nutrisari")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== STRUK PEMBELIAN =========")
print("==================================")
print ("Nama\t\t:",nama)
print ("Alamat\t\t:",Alamat)
print ("No_telp\t\t:",No_telp)
print ("Tanggal\t\t:",Tanggal)



print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")