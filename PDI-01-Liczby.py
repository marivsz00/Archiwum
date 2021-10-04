#!/usr/bin/env python
# encoding: utf-8

"""
PYTHON DLA INŻYNIERÓW
Lekcja: #1 Wprowadzenie + Liczby

Copyright: Łukasz Zdanowicz | www.oprojektowaniu.pl
"""

# ==========================================================================
# 3. Operacje arytmetyczne
# ==========================================================================

# Dodawanie
print(1+2)

# Odejmowanie
print(3-2)

# Mnożenie
print(2*2)

# Dzielenie w Python 3
print(3/2)

# --------------------------------------------------------------------------
# Uwaga do Pythona 2
# --------------------------------------------------------------------------

# Pierwszy sposób: Zmiana przynajmniej jednej liczby na liczbę zmiennoprzecinkową
print(3.0/2)

# Działa to dla którejkolwiek z liczb
print(3/2.0)

# Drugi sposób: Zamiana liczby całkowitej na zmiennoprzecinkową za pomocą funkcji float()
print(float(3)/2)

# --------------------------------------------------------------------------
# Działania arytmetyczne - ciąg dalszy
# --------------------------------------------------------------------------

# Potęgowanie
print(2**3)

# Do potęgowania możemy wykorzystać również funkcję:
print(pow(2,3))

# Wyrażenie potęgowe 'e'
print(3e2)

# Pierwiastek możemy otrzymać korzystając z funkcji potęgowania
print(4**(0.5))

# Funkcja pow() też się do tego nadaje
print(pow(4, 0.5))

# Kolejność działań w Pythonie
print(1 + 10 * 10 + 2)

# Do określenia kolejności działań możemy użyć nawiasów okrągłych
print((1+10) * (10+2))

# Przykład z liczbami ujemnymi
print((-7 + 2) * (-4))

# Wartość bezwzględna z liczby
print(abs(-2))

# Wartość maksymalna ze zbioru liczb
print(max(1,8,-10,5))

# Wartość minimalna ze zbioru liczb
print(max(1,8,-10,5))

# Zaokrąglenie z domyślną dokładnością
print(round(3.1415))

# Zaokrąglenie z zadaną dokładnością
print(round(3.1415, 2))     # Do dwóch miejsc po przecinku

# Przykład zaokrąglenia innej liczby
print(round(123.456, 1))    # Do jednego miejsca po przecinku
print(round(123.456, -1))   # Zaokrąglenie do pełnych 10
print(round(123.456, -2))   # Zaokrąglenie do pełnych 100

# ==========================================================================
# 4. Definiowanie zmiennych
# ==========================================================================

# Stwórzmy obiekt o nazwie 'x' i przypiszmy mu wartość 5
x = 5

# Wywołanie 'x'
print(x)

# Dodawanie obiektów
print(x + x)

# Przypisanie zmiennej nowej wartości
x = 15

# Wywołanie 'x'
print(x)

# Mamy zmienną 'x' o wartości 15:
x = 15

# Użyj `x` do przypisania jej nowej wartości równej 'x + x':
x = x + x
print(x)

# ==========================================================================
# 5. Przykład obliczeniowy (Eurokod 2)
# ==========================================================================

# Dane
fck = 30                    # Wartość w [MPa]

# Obliczenia wg EC2
fcm = fck + 8               # Średnia wytrzymałość betonu na ściskanie [MPa]

Ecm = 22*(0.1*fcm)**0.3     # Sieczny moduł sprężystości betonu [GPa]

# Wynik
print(round(Ecm,1))
