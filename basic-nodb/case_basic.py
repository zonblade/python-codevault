# sampel pengguanaan switch

# definisikan dulu function
# yang akan digunakan didalam switch,
# boleh menggunakan class jika ingin private function
def case_1():
	return 'case 1'
def case_2():
	return 'case 2'
def case_3():
	return 'case 3'

# setelah semua case di definisikan
# buatlah function untuk switch casenya.
# buat switch dengan isi object seperti dibawah
def case_switcher(case):
	switch = {
		'case1':case_1(),
		'case2':case_2(),
		'case3':case_3(),
	}
	# case disini mengambil parameter key dari object
	# jadi case input akan disamakan dengan key yang sama
	return switch.get(case)

# coba hasilnya
print(
	case_switcher('case1')
)
