print("programdan çıkmak için 'exit' yazın")
while True:
   girdi = input("Sayı girin : ")
   if (girdi == "exit"):
       break
   else:
       girilenSayi=int(girdi)
       sonuc=0
       girilenSayi=int(girilenSayi)
       liste=[]
       for i in range(1,girilenSayi):
           if girilenSayi%i==0:
               liste.append(i)
       for m in liste:
           sonuc=sonuc+m
       if (sonuc==girilenSayi):
           print ('Mükemmel Sayı')
       elif (sonuc<girilenSayi):
           print('Eksik Sayı')
       else:
           print ('Artık Sayı')