# #membuat gabungan area rentang dari angka

# #+++++3-----10+++++++
# inputus=float(input('masukan angka yang bernilai\n kurang dari 3 \n lebih dari 10: \n'))


# # ++++++3-------------
# #memeriksa angka kurang dari 3
# iskurangdari=(inputus < 3)
# print(inputus,' kurang dari 3 =',iskurangdari)

# # ++++++3-------------
# #memeriksa angka kurang dari 3
# islbhdri=(inputus > 10)
# print(inputus,' Lebih dari 10 =' ,islbhdri)



# isbnr = iskurangdari or islbhdri
# print('angka yang anda masukan:',isbnr)



#kasus irisan 
inputus=float(input('masukan angka yang bernilai\n lebih dari 3 \n dan kurang dari 10 \n :'))

#islebih dari
islebihdari = inputus > 3
print(inputus,' lebih dari 3 =',islebihdari)

#kurang dari
#islebih dari
iskrng = inputus < 10
print(inputus,' lebih dari 10 =',iskrng)

hasil = islebihdari and iskrng
print('apakah keduanya memenuhi:',hasil)