# cara menggunakan def
# pada dasarnya def anything(**args,**kwargs)

# mendefinisikan fungsi apapun()
# tanpa men-set default value
def apapun_contoh1(teks):
  return teks

# jika di print naked/atau tanpa value akan error
apapun_contoh1()        # TIDAK valid
apapun_contoh1('hello') # valid

# jadi sebaiknya setiap membuat fungsi
# set lah default valuenya, sebagai berikut
def apapun_contoh2(teks=''):
  return teks

# jika di print naked/ ata tanpa value akan baik baik saja
apapun_contoh2()        # valid!
apapun_contoh2('hello') # valid!
