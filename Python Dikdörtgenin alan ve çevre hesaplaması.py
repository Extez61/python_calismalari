def dikdorgen(kisa, uzun):
   alan = int(kisa) * int(uzun)
   cevre = 2 * (int(kisa) + int(uzun))
   print("Alan :", alan)
   print("çevre :", cevre)
   return alan,cevre
kisakenar=input('Kısa Kenar : ')
uzunkenar=input('Uzun Kenar : ')
dikdorgen(kisakenar,uzunkenar)