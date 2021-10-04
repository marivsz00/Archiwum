# Dla wczytanej z klawiatury liczby naturalnej n sprawdza, czy liczba ta jest pierwsza

n = input()
n = int(n)
flaga = True
for dzielnik in range(2, n):
    if n % dzielnik == 0:
        flaga = False
if flaga == True:
    print("Jest to liczba pierwsza")
else:
    print("Nie jest to liczba piersza")
    