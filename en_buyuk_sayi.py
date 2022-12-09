liste=[]


while True:
   sayi = input('Sayıyı Gir (sayı girme işleiniz bittiğinde ise "ok" yazarak işlerimi bitirebilirsiniz): ')
   if (sayi == "ok"):
       print("listede toplam {0} eleman var ve ".format(len(liste)), "en büyük sayı: ", max(liste), "en küçük sayı: ", min(liste))
       print(liste)
       break
   else:
       liste.append((sayi))
    #    print(type(sayi))
       print("\n")
       liste.append(int(sayi))
       print(type(sayi))
       print("\n")
       continue