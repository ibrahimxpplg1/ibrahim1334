print("selamat datang di dafun")
nama=input("siapa namamu")
umur=input("berapa umurmu")
print("halo ibrahim selama menikmati wahana di dafun")

print("daftar wahana")
daftar_wahana=["biang lala Rp. 13.000", "istana boneka Rp. 10.000", "rumah kaca Rp. 15.000", "roaller coaster Rp. 20.000"]

angka = 1
for daftar_wahana in daftar_wahana:
    print(str(angka), '.',daftar_wahana)
    angka = int(angka) + 1
input("pilih nomor wahana")
if("nomor == 1"):
    print("tiket = Rp. 13.000")