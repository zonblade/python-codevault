# any() 
# berguna untuk pengecekan secara singkat dan cepat.


# untuk mengecek apakah ada angka
# lebih besar atau kecil
# sesuaikan > < !=  saja.
# tidak harus angka bisa yang lainnya juga.
angka = [2,2,3,4]
number = 2
if any(item < number for item in angka):
	print(f'ada angka kurang dari {number}')
else:
	print(f'tidak ada angka kurang dari {number}')

# berguna untuk mempersingkat kode.
# any mencari ketemu pada pengkondisian
# yang didefinisikan.


# berlaku juga untuk teks
# misal mau mengecek apakah ada int di daftar teks
# dengan singkat
teks  = 'abcdef092'
if any(item.isdigit() for item in teks):
	print('ada angka dalam teks')
else:
	print('tidak ada angka dalam teks')
