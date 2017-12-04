phonebook = {'Rüzgar': 8806336,
             'Ozan': 6784346,
             'Yasar Universitesi': 7658344,
             'Tostcu Erol': 1122345}  # Dictionary

print(phonebook['Rüzgar'])

sozluk = {1: 'Bir', 'iki': 2}

print(sozluk[1])
print(sozluk['iki'])

print(sozluk.items())
print(sozluk.keys())
print(sozluk.values())

del sozluk['iki']
print(sozluk)
