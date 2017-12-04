sayi1 = int(input("Lütfen 1.sayıyı girin : "))
sayi2 = int(input("Lütfen 2 sayıyı girin : "))

print('Toplam: {} \nÇıkarma: {}\nBölüm: {}\nÇarpım: {}'.format('+', '-', '/', '*'))

operator = input("İşlem girin: ")
if operator == "+":
    sonuc = sayi1 + sayi2
    print('{} + {} = {}'.format(sayi1, sayi2, sonuc))
elif operator == "-":
    sonuc = sayi1 - sayi2
    print('{} - {} = {}'.format(sayi1, sayi2, sonuc))
elif operator == "/":
    sonuc = sayi1 / sayi2
    print('{} / {} = {}'.format(sayi1, sayi2, sonuc))
elif operator == "*":
    sonuc = sayi1 * sayi2
    print('{} * {} = {}'.format(sayi1, sayi2, sonuc))
else:
    print("Lütfen Geçerli Bi İşlem yap")
