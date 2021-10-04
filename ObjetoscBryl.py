#Napisz program z “konsolowym menu” (za pomocą komendy print wyświetl możliwe dla użytkownika opcje,
#poprzedzając je kolejnymi cyframi 1…2…, a następnie poproś użytkownika o wpisanie cyfry odpowiadającej wyborowi).
#Program ma pytać użytkownika jakiej figury pole chce obliczyć.

#Program powinien liczyć pola: kwadratu, prostokąta, trójkąta, trapezu, równoległoboku.
import math

print("Witaj, w tym programie możesz obliczyć pole figur oraz objętość brył")
forbryl = int(input("""Wybierz z poniższych opcji co chcesz obliczyć
1.Chcę obliczyć pole
2.Chcę obliczyć objętość
Mój wybór to:"""))

#POLE
if forbryl == 1:
    print("Wybrałeś opcję 1")
    wybor = int(input("""Spośród poniższych opcji, wybierz figurę,której pole chcesz obliczyć:
    1.Kwadrat
    2.Prostokąt
    3.Trójkąt
    4.Trapez
    5.Równoległobok
    Mój wybór to: """))
    #Kwadrat
    if wybor == 1:
        boka1 = float(input("Podaj długość boku kwadratu: "))


        polekw = boka1**2

        print("Pole tego kwadratu wynosi {}".format(polekw))
    #Prostokąt
    elif wybor == 2:
        boka2 = float(input("Podaj długość pierszego boku: "))
        bokb2 = float(input("Podaj długość drugiego boku: "))

        poleprost = boka2*bokb2

        print("Pole tego prostokąta wynosi: {}".format(poleprost))
    #Trójkąt
    elif wybor == 3:
        podstawa3 = float(input("Podaj długość podstawy: "))
        wysokosc3 = float(input("Podaj wysokość: "))

        poletroj = (podstawa3*wysokosc3)/2

        print("Pole tego trójkąta wynosi: {}".format(poletroj))
    #Trapez
    elif wybor == 4:
        podstawa4a =float(input("Podaj długość pierwszej z podstaw: "))
        podstawa4b =float(input("Podaj długość drugiej z podstaw: "))
        wysokosc4 = float(input("Podaj wysokość: "))

        poletrap = ((podstawa4a+podstawa4b)/2)*wysokosc4

        print("Pole tego trapezu wynosi: {}".format(poletrap))
    #Równoległobok
    elif wybor == 5:
        podst_rownoleglobok = float(input("Podaj długość podstawy: "))
        wysokosc_rownoleglobok = float(input("Podaj wysokość: "))

        polerown = podst_rownoleglobok*wysokosc_rownoleglobok

        print("Pole tego równoległoboku wynosi: {}".format(polerown))

    else:
        print("Zrestartuj program i wprowadz poprawna liczbe!")
#OBJETOSC
elif forbryl == 2:
    print("Wybrales opcję 2")

    wybor2 = int(input("""Spośród poniższych opcji wybierz bryłę, której objętość chcesz obliczyć: 
    1.Sześcian
    2.Prostopadłościan
    3.Walec 
    4.Kula
    Mój wybór to: """))

    if wybor2 == 1:
        bokAszescian = float(input("Wprowadz długość boku sześcianu: "))
        objszescian = bokAszescian**3
        print("Objętość tego sześcianu wynosi: {}".format(objszescian))

    elif wybor2 == 2:
        bokAprost = float(input("Wprowadz dlugosc boku A: "))
        bokBprost = float(input("Wprowadz długość boku B: "))
        bokCprost = float(input("Wprowadz długość boku C: "))

        objprost = bokAprost*bokBprost*bokCprost

        print("Objętość tej figury wynosi: {}".format(objprost))


    elif wybor2 == 3:

        promienwalec = float(input("Wprowadz promień walca: "))
        wysokoscwalec = float(input("Wprowadz wysokość walca: "))
        objwalec1 = (math.pi)*(promienwalec**2)*(wysokoscwalec)
        print("Objętość tego walca wynosi: {}".format(objwalec1))
    elif wybor2 == 4:
        promienKula = float(input("Wprowadz promien kuli: "))
        objKuli = (4 / 3) * (math.pi) * (promienKula ** 3)
        print("Objętość tej kuli wynosi: {}".format(objKuli))

else:
    print("Zrestartuj program i wpisz właściwą liczbę!")
