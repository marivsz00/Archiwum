#rodzaje pętli
for iterator in range(10):
    print("Test", iterator)

#range() - ile razy ma się coś powtórzyć
#iterator - przechowuje wartości od 0 do 10(w tym przypadku)
#range() może przyjmować różne wartości np 5 i 10
for iterator in range(5, 10):
    print("test", iterator)

#można tez zrobic co 2 np (0, 10, 2)
#np parzyste (0, 10, 2)
#np nieparzyste (1, 10, 2)
#Jeśli nie zrobimy wcięcia, pętla się zakończy

#petli for najlepiej uzywac wtedy kiedy wiemy jaki jest
# zakres np petla ma zadzialac 10 razy

#pętli while uzywamy wtedy kiedy nie wiemy ile razy sie ma wykonac
i=5
while i < 10:
    print(i)
    i=i+1
print("Koniec")
#wypisze wtedy liczby od 5 do 9
#dopóki i < 10 to wykonuj

i = 5000
while i > 2:
    print(i)
    i = i /35
    i = i + 3
    i = i / 2
print("Koniec")

# CTRL + / zakomentuje całe zaznaczone pole, jak kliknie się znowu to wróci

# Występują także pętle until
#pętle można zagnieżdżać, zatrzymywać, kontynuować


#przerywanie pętli
for iterator in range(5, 10):
    print(iterator)
    if iterator == 5:
        print("Stop")
        break
    print("Lece dalej", iterator)
print("koniec")

#kontynuowanie pętli
for iterator in range(5, 10):
    print("Start", iterator)
    if iterator == 5:
        print("Stop")
        continue
    print("Lece dalej", iterator)
print("koniec")
#gdy iterator jest równy 5 continue pomija "Lece dalej"





#napisy

dlugosc = len("Ala ma kota")
print(dlugosc)
#spacja też jest liczona
#funckcja len zwraca dlugosc tekstu

for i in slowo:
    print(i)

#W tym przypadku iteratorem bylo slowo
#Warto iterator nazywac
#powinno nazywać sie zmienne tak zeby druga osoba(programista) czytajaca kod wiedziala o co chodzi


#Wypisz piątą literę ze slowa

slowo = "Ala ma kota"
print(slowo[4])
# jest to 4 ponieważ zaczyna liczyć od 0

#pętla w pętli

for iterator in range(10):
    print("Iterator:", iterator)
    for licznik in range(5):
        print("Licznik: ", licznik)
    print("Koniec wenetrznej petli")

#

print(len("Ala")/2)

#funkcja lower case upper case
# zmienia na male lub duze litery

#funkcja islower oraz is upper ----> zwraca Prawde lub fałsz
print(len"Ala".isupper())

#funkcja capitalize -----> zmienia pierwszą literę na dużą
print("Ala".capitalize())

#zaokrąglanie liczb zmiennoprzecinkowych(2 sposoby)
#wymuszenie zaokraglenia
print(int(1.191))
#matematyczne zaokraglenie
#najpierw trzeba dodac biblioteke matematyczna
import math
print(math.ceil(1.191))
#integer ---> liczba całkowita



