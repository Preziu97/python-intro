import time


def sprawdz_email(email):
    if "@" not in email:
        return False

    lokalna_czesc, domena = email.split("@", 1)

    if len(lokalna_czesc) == 0:
        return False

    if domena.startswith("."):
        return False

    if "." not in domena:
        return False

    czesc_po_kropce = domena.split(".")[-1]
    if len(czesc_po_kropce) < 2:
        return False

    if len(domena) < 4:
        return False

    return True

def oblicz_pole_kwadratu(a):
    return a ** 2


def filtruj_i_sortuj(lista):
    przefiltrowana_lista = [x for x in lista if x > 10]
    przefiltrowana_lista.sort()
    return przefiltrowana_lista


def konwertuj_date(data, stary_format, nowy_format):
    try:
        data_obj = time.strptime(data, stary_format)
        nowa_data = time.strftime(nowy_format, data_obj)
        return nowa_data
    except ValueError:
        return None


def sprawdz_palindrom(tekst):
    tekst = tekst.replace(" ", "").lower()
    return tekst == tekst[::-1]