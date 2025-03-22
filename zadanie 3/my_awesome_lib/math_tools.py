def add(a, b):
    """
    Dodaje dwie liczby.

    Argumenty:
    a (int, float): Pierwsza liczba.
    b (int, float): Druga liczba.

    Zwraca:
    int, float: Suma liczb a i b.

    Przykład:
    >>> add(3, 5)
    8
    """
    return a + b


def subtract(a, b):
    """
    Odejmuje dwie liczby.

    Argumenty:
    a (int, float): Liczba, od której odejmujemy.
    b (int, float): Liczba, którą odejmujemy.

    Zwraca:
    int, float: Różnica między liczbami a i b.

    Przykład:
    >>> subtract(10, 4)
    6
    """
    return a - b


def multiply(a, b):
    """
    Mnoży dwie liczby.

    Argumenty:
    a (int, float): Pierwsza liczba.
    b (int, float): Druga liczba.

    Zwraca:
    int, float: Iloczyn liczb a i b.

    Przykład:
    >>> multiply(2, 3)
    6
    """
    return a * b


def divide(a, b):
    """
    Dzieli dwie liczby.

    Argumenty:
    a (int, float): Liczba dzielona.
    b (int, float): Liczba, przez którą dzielimy.

    Zwraca:
    float: Wynik dzielenia liczby a przez b.

    Wyjątki:
    - ZeroDivisionError: Jeśli b jest zerem, zwróci komunikat o błędzie.

    Przykład:
    >>> divide(6, 3)
    2.0
    >>> divide(5, 0)
    "Błąd: dzielenie przez zero"
    """
    if b == 0:
        return "Błąd: dzielenie przez zero"
    return a / b
