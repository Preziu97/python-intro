def add_element(data, element):
    """
    Dodaje element do listy.

    Argumenty:
    data (list): Lista, do której dodajemy element.
    element (int, float, str, itp.): Element, który chcemy dodać do listy.

    Zwraca:
    None: Funkcja modyfikuje listę w miejscu, nie zwraca żadnej wartości.

    Przykład:
    >>> lista = [1, 2, 3]
    >>> add_element(lista, 4)
    >>> lista
    [1, 2, 3, 4]
    """
    data.append(element)


def merge_data(data1, data2):
    """
    Łączy dwie listy.

    Argumenty:
    data1 (list): Pierwsza lista.
    data2 (list): Druga lista, którą łączymy z pierwszą.

    Zwraca:
    list: Nowa lista będąca połączeniem obu list.

    Przykład:
    >>> lista1 = [1, 2]
    >>> lista2 = [3, 4]
    >>> merge_data(lista1, lista2)
    [1, 2, 3, 4]
    """
    return data1 + data2


def remove_duplicates(data):
    """
    Usuwa duplikaty z listy.

    Argumenty:
    data (list): Lista, z której usuwamy duplikaty.

    Zwraca:
    list: Nowa lista bez duplikatów.

    Przykład:
    >>> lista = [1, 2, 2, 3, 4, 4, 5]
    >>> remove_duplicates(lista)
    [1, 2, 3, 4, 5]
    """
    return list(set(data))