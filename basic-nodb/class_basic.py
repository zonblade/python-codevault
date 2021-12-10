# cara membuat class
# refrensi string formatting : https://realpython.com/python-f-strings/

# membuat class.
class nama:
	# function didalam class sudah termasuk private function
	# konstruksi awal 
	def __init__(self,val_awal):
		# mendefinisikan value awal
		# boleh banyak
		self.val_awal = val_awal
	
	# untuk menggunakan self 
	# harus di definisikan lagi pada function didalam class
	def apapun(self,val_lain):
		# return dengan format string
		# agar dapat menggunakan bracket didalamnya.
		return f'dari awal: {self.val_awal}, dari fungsi: {val_lain}'

# penggunaan
# kita akan mengisi val awal dengan hello.
# bisa sebagai pengkondisian
obj = nama('hello')

# jika ingin menggunakan private function
# dapat menggunakan dot chaining seperti dibawah.
hasil = obj.apapun('value lain')

# hasil
print(hasil)

# dari awal: hello, dari fungsi: value lain
