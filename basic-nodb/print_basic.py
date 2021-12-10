nama  = 'bambang'
kelas = 'barusu'

# print biasa
print(
	'hello world'
)

# print dengan format langsung
# paling enak udah
print(
	f'namaku: {nama}, kelas: {kelas}'
)

# print dengan format terpisah menggunakan index
# berguna untuk membolak balik format
print(
	'namaku: {0}, kelas: {1}'.
	format(nama,kelas)
)

# print dengan format terpisah menggunakan urutan
# berguna untuk formating angka
print(
	'namaku: %s, kelas: %s' 
	% (nama,kelas)
)

# cheatsheet format persen
# %s  = input any    output string
# %0d = input number output int
# %0f = input number output float
# %0o = input number output octal
# %0E = input number output exponential
