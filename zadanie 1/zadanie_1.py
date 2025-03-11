'''
Opis funkcji zip()
Funkcja zip() umożliwia równoczesne iterowanie po kilku obiektach iterowalnych,
tworząc krotki zawierające elementy z każdego z nich. Innymi słowy, łączy elementy
z podanych iterowalnych obiektów w pary (lub większe krotki, jeśli podano więcej iterowalnych).
Dokumentacja: https://docs.python.org/3/library/functions.html#zip
'''
print("Przykład działania funkcji zip():")
lista1 = [1, 2, 3] # Lista 1
lista2 = ['a', 'b', 'c'] # Lista 2
wynik = list(zip(lista1, lista2)) # Polaczenie list
print(wynik)
'''
Opis funkcji enumerate()
enumerate() to wbudowana funkcja w Pythonie, która pozwala na iterowanie po sekwencji
(np. liście, krotce) i jednoczesne śledzenie indeksów elementów w tej sekwencji.
Zwraca obiekt typu enumerate, który jest iterowalny, a każde jego wywołanie zwraca krotkę
składającą się z indeksu i wartości elementu z oryginalnej sekwencji.

Składnia:
enumerate(iterable, start=0)
iterable – sekwencja, po której chcemy iterować.
start – opcjonalny argument, który pozwala ustawić początkowy indeks (domyślnie jest to 0).

Dokumentacja: https://docs.python.org/3/library/functions.html#enumerate.
'''
print("\nPrzykład działania funkcji enumerate():")
lista = ['a', 'b', 'c'] # Stowrzenie listy
for index, value in enumerate(lista): # Numerowanie elementów listy
    print(index, value)

'''
Opis funkcji sorted()
Funkcja sorted() w Pythonie jest używana do sortowania iterowalnych obiektów 
(takich jak listy, krotki, ciągi tekstowe itp.) w porządku rosnącym lub malejącym. 
Funkcja ta zwraca nową posortowaną listę, pozostawiając oryginalny obiekt bez zmian.

Składnia:
sorted(iterable, key=None, reverse=False)
iterable – obiekt, który chcesz posortować (np. lista, krotka, ciąg znaków).
key – opcjonalny argument, który pozwala określić funkcję, po której będzie wykonywane sortowanie. 
Funkcja key jest stosowana do każdego elementu przed porównaniem.
reverse – opcjonalny argument (domyślnie False), który pozwala na posortowanie w porządku malejącym, 
jeśli ustawisz True.

Dokumentacja: https://docs.python.org/3/library/functions.html#sorted
'''
print("\nPrzykład działania funkcji sorted():")
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
posortowana_lista = sorted(lista) # Sortowanie listy
print(posortowana_lista)

'''
Opis modulu math
Moduł math w Pythonie dostarcza funkcji matematycznych do wykonywania różnych obliczeń matematycznych, 
takich jak funkcje trygonometryczne, logarytmy, obliczanie pierwiastków, stała pi, itp.

Dokumentacja: https://docs.python.org/3/library/math.html
'''

print("\nPrzykład działania modułu math:")
import math
wynik = math.sqrt(16) # Pierwiastek z 16
print(wynik)
print(math.pi) # Wyświetlenie liczby pi

'''
Opis modułu random
Moduł random w Pythonie pozwala na generowanie losowych liczb oraz operacje związane z losowością, 
np. losowanie elementów z listy, tasowanie elementów.

Dokumentacja: https://docs.python.org/3/library/random.html
'''
print("\nPrzykład działania modułu random:")
import random
liczba = random.randint(1, 10) # Losuje liczbe od 1 do 10
print(liczba)

'''
Opis modułu time
Moduł time w Pythonie jest używany do pracy z czasem. Umożliwia m.in. 
uzyskiwanie bieżącego czasu, mierzenie czasu wykonywania kodu, opóźnianie wykonywania programu.

Dokumentacja: https://docs.python.org/3/library/time.html
'''
print("\nPrzykład działania modułu time:")
import time
czas = time.localtime()  # Zwraca bieżący czas w formie struktury
sformatowany_czas = time.strftime("%Y-%m-%d %H:%M:%S", czas)
print(sformatowany_czas)

'''
Opis wyjątku ValueError
ValueError jest jednym z wbudowanych wyjątków w Pythonie, który jest używany, 
gdy operacja lub funkcja otrzymuje argument o nieodpowiedniej wartości, ale o poprawnym typie.

Dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError
'''
print("\nPrzykład działania wyjatku ValueError")
print("UWAGA! W celu przetesotwania wyjatku nalezy podac inna liczbe niz calkowita")
def wczytaj_liczbe():
    while True:
        try:
            # Poproszenie o wprowadzenie liczby
            liczba = int(input("Wprowadź liczbę całkowitą: "))
            print(f"Wprowadzona liczba to: {liczba}")
            break  # Zakończ pętlę, gdy użytkownik poda poprawną liczbę
        except ValueError:
            # Obsługa błędu, gdy użytkownik nie poda liczby całkowitej
            print("Błąd: To nie jest liczba całkowita! Spróbuj ponownie.")

wczytaj_liczbe()
'''
Opis wyjątku ZeroDivisionError
ZeroDivisionError jest wyjątkiem, który występuje, gdy próbujesz podzielić liczbę przez zero lub 
wykonać operację modulo przez zero.

Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
'''
print("\nPrzykład działania wyjatku ZeroDivisionError")
print("UWAGA! W celu przetesotwania wyjatku nalezy podzielić przez zero")
print("Kalkulator dzielenia:")
def dzielenie():
    while True:
        try:
            # Pobierz dwie liczby od użytkownika
            a = float(input("Wprowadź pierwszą liczbę: "))
            b = float(input("Wprowadź drugą liczbę: "))

            # Próba podzielenia
            wynik = a / b
            print(f"Wynik dzielenia {a} przez {b} to: {wynik}")
            break  # Zakończ pętlę po poprawnym dzieleniu

        except ZeroDivisionError:
            # Obsługa błędu: dzielenie przez zero
            print("Błąd: Nie można dzielić przez zero! Spróbuj ponownie.")

dzielenie()
