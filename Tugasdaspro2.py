hari_kerja = 15
hari_kerja_perbulan = 20
gaji = 500000
tarif_lembur = 200000 

# Menghitung gaji biasa
gaji_biasa = (hari_kerja / hari_kerja_perbulan) * gaji

# Menentukan apakah ada lembur
if hari_kerja > hari_kerja_perbulan:
    hari_lembur = hari_kerja - hari_kerja_perbulan
    gaji_lembur = hari_lembur * tarif_lembur * gaji
else:
    hari_lembur = 2
    gaji_lembur = 200000

# Menghitung total gaji dengan lembur
total_gaji = gaji_biasa + gaji_lembur

# Mengganti koma menjadi titik pada nilai gaji
total_gaji_str = "{:,.2f}".format(total_gaji).replace(",",".")

print ("Total_gaji selama 15 hari/1 Bulan : Rp.", total_gaji_str)
print("Jumlah hari lembur:", hari_lembur)
print("Total gaji lembur: Rp.", "{:,.2f}".format(gaji_lembur).replace(",", "."))