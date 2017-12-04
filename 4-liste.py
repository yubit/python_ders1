liste1 = ['Kedi', 'Kopek', 'Akrep', 'Balik']
liste2 = [1000, 1337, 4500]
liste3 = ['Kedi', 'Kopek', 1000, 1337, 'Balik', 'Akrep', 4500]  # List

print(liste1)
print(liste2)
print(liste3)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # List

print('len', len(liste))  # Listedeki eleman sayisi

print('[2:5]', liste[2:5])  # Listede 2. eleman(2.Eleman dahil değil) ile 5. eleman(5.eleman dahil) arasinda bulunan elemanlar

print('[-1]', liste[-1])  # sondan ilk eleman

print('[2::2]', liste[2::2])  # Listede 2 eleman arttırarak ekrana yazdırma

print('[:2]', liste[:2])  # Listeki ilk 2 elemanı ekrana yazdırmak

print('index 3', liste.index(3))

liste.append(10)  # Listeye 10 elamanını eklemek
print('append(10)', liste)  # Yeni eleman eklendikten sonra ekrana yazdırması

liste.remove(3)  # Listedeki 3 elemanını listeden çıkarmak
print('remove(3)', liste)  # Listedeki

liste.append('Python')  # Listeye string eklemek
print("append('Python')", liste)  # Guncel listeyi ekrana yazdırması

liste.remove('Python')  # String olan elamanları listeden silmek
print("remove('Python')", liste)  # Guncel listeyi ekrana yazdırması

del liste[0]  # Listedeki 1. elamanı siler çünkü listede elemanlar 0 dan başlar
print("del 0", liste)  # Guncel listeyi ekrana yazdırması

del liste[1]  # Guncel Listedeki 2. elemanı siler
print("del 1", liste)

liste.reverse()
print('reverse', liste)  # Listeyi tersine çevirir

sayilar = (1, 2, 3, 4, 5, 5)  # tuple
print('Sayılar', sayilar)

kume = set(sayilar)
print('Küme', kume)
