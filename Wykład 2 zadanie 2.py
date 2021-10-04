# Sprawdza, czy wczytana z klawiatury liczba jest palindromem, tzn. czytana
# od końca jest taka sama np. 12321, 234432, 3445

wyraz = input("Podaj wyraz")
dlugosc = len(wyraz)

# print(wyraz[0])
# print(wyraz[dlugosc-1])
#
# print(wyraz[1])
# print(wyraz[dlugosc-2])


licznik = dlugosc
flaga = True

for znak in wyraz:
    print(znak, wyraz[licznik - 1])
    if znak != wyraz[licznik - 1]:
        flaga = False
        break
    licznik = licznik - 1
if flaga == True:
    print("Jest to palindrom")
else:
    print("Nie jest to palindrom")