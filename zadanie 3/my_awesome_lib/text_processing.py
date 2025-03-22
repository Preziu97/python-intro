import string


def count_words(text):
    """
    Liczy liczbę słów w tekście.

    Argumenty:
    text (str): Tekst, w którym liczymy słowa.

    Zwraca:
    int: Liczba słów w tekście.

    Przykład:
    >>> count_words("Ala ma kota")
    3
    """
    words = text.split()
    return len(words)


def remove_punctuation(text):
    """
    Usuwa wszystkie znaki interpunkcyjne z tekstu.

    Argumenty:
    text (str): Tekst, z którego usuwamy znaki interpunkcyjne.

    Zwraca:
    str: Tekst bez znaków interpunkcyjnych.

    Przykład:
    >>> remove_punctuation("Hello, world!")
    'Hello world'
    """
    return text.translate(str.maketrans('', '', string.punctuation))


def reverse_text(text):
    """
    Odwraca tekst.

    Argumenty:
    text (str): Tekst, który chcemy odwrócić.

    Zwraca:
    str: Odwrócony tekst.

    Przykład:
    >>> reverse_text("Ala")
    'alA'
    """
    return text[::-1]
