# definisikan fungsi agar lebih simpel
def textCleanup(text='',param='',mode='clean'):
	# pecah teks yang diinput 
	for X in text:
		# breakdown huruf yang ingin disingkirkan
		# menggunakn list
		# disini menggunakan replace kosong,
		# untuk setiap huruf yang ingin dibuang
		if mode == 'reserve' and X not in list(param):
			# jika modenya reserve akan menyimpan
			# teks yang terdefinisi
			text = text.replace(X,'') 
		elif mode == 'clean' and X in list(param):
			# jika modenya clean akan menghilangkan 
			# teks yang terdefinisi
			text = text.replace(X,'')
	# return valuenya.
	return text

# coba hasilnya
print(
	textCleanup(
		text  = 'hello world',
		param = 'ow',
		mode  = 'clean'
	)
)

# mode clean : hell rld
# mode reserve : owo
