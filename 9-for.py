# aralik = range(0, 10)
# print(aralik, type(aralik))
#
# for sayi in range(0, 10):
#     print(sayi)

# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(liste, type(liste))
#
# for sayi in range(0, len(liste) + 1):
#     print(sayi)

"""cift_sayilar = range(0, 10, 2)

for sayi in cift_sayilar:
    print(sayi)"""

iki_boyutlu = [
    [1, 2],
    [3, 4],
    [5, 6]
]

"""for satir in iki_boyutlu:
    print(satir)"""

"""for satir in iki_boyutlu:
    for sutun in satir:
        print(sutun)"""
# ilk,iki = 1,2
# for ilk, iki in iki_boyutlu:
#     print(ilk, iki)

phonebook = {'Rüzgar': 8806336, 'Ozan': 6784346, 'Yasar Universitesi': 7658344, 'Tostcu Erol': 1122345}

for isim, numara in phonebook.items():
    print("{}: {}".format(isim, numara))
    print(isim, ':', 'numara')

isim = 'rüzgar'
isim.