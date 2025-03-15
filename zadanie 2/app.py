def sprawdz_email(email):
    return "@" in email and "." in email.split("@")[-1]


email = input("Podaj adres e-mail: ")

if sprawdz_email(email):
    print("Adres e-mail jest poprawny.")
else:
    print("Adres e-mail jest niepoprawny.")


def oblicz_pole_kwadratu(a):
    return a ** 2


a = float(input("Podaj długość boku kwadratu: "))

pole = oblicz_pole_kwadratu(a)

print(f"Pole kwadratu o boku {a} wynosi: {pole}")


def filtruj_i_sortuj(lista):
    przefiltrowana_lista = [x for x in lista if x > 10]

    przefiltrowana_lista.sort()

    return przefiltrowana_lista


dane = [5, 10, 15, 3, 22, 8, 12, 7]

wynik = filtruj_i_sortuj(dane)

print("Przefiltrowana (liczby powyżej 10) i posortowana lista:", wynik)

import time


def konwertuj_date(data, stary_format, nowy_format):

    data_obj = time.strptime(data, stary_format)

    nowa_data = time.strftime(nowy_format, data_obj)

    return nowa_data


data = input("Podaj datę (np. 15-03-2025): ")
stary_format = "%d-%m-%Y"  # format: dzień-miesiąc-rok
nowy_format = "%Y/%m/%d"  # format: rok/miesiąc/dzień

nowa_data = konwertuj_date(data, stary_format, nowy_format)

print("Nowy format daty:", nowa_data)

import time


def konwertuj_date(data, stary_format, nowy_format):
    try:
        data_obj = time.strptime(data, stary_format)

        nowa_data = time.strftime(nowy_format, data_obj)

        return nowa_data
    except ValueError:
        return None


while True:
    data = input("Podaj datę (np. 15-03-2025): ")
    stary_format = "%d-%m-%Y"
    nowy_format = "%Y/%m/%d"

    nowa_data = konwertuj_date(data, stary_format, nowy_format)

    if nowa_data:
        print("Nowy format daty:", nowa_data)
        break
    else:
        print("Błędny format daty. Spróbuj ponownie.")
