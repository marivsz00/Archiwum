
print("Witaj, ten program pomoże sprawdzić, czy podany przez Ciebie numer PESEL jest poprawny")
print("""Gdy na ekranie ukaże się monit o wprowadzenie pierwszej cyfry numeru PESEL,
zacznij go wpisywać, upewniając się, że po każdej z cyfr klikasz ENTER""")

c1 = int(input("Wprowadź 1 cyfrę: "))
c2 = int(input("Wprowadź 2 cyfrę: "))
c3 = int(input("Wprowadź 3 cyfrę: "))
c4 = int(input("Wprowadź 4 cyfrę: "))
c5 = int(input("Wprowadź 5 cyfrę: "))
c6 = int(input("Wprowadź 6 cyfrę: "))
c7 = int(input("Wprowadź 7 cyfrę: "))
c8 = int(input("Wprowadź 8 cyfrę: "))
c9 = int(input("Wprowadź 9 cyfrę: "))
c10 = int(input("Wprowadź 10 cyfrę: "))
c11 = int(input("Wprowadź 11 cyfrę: "))

if ((c1*1)+(c2*3)+(c3*7)+(c4*9)+(c5*1)+(c6*3)+(c7*7)+(c8*9)+(c9*1)+(c10*3)+(c11*1)) % 10 == 0:
    print("Ten PESEL jest poprawny")
else:
    print("Ten PESEL jest niepoprawny")
