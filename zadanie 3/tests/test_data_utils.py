import unittest
from my_awesome_lib.data_utils import add_element, merge_data, remove_duplicates


class TestDataTools(unittest.TestCase):

    def setUp(self):
        """Inicjalizacja danych testowych"""
        # Lista do testów dla add_element
        self.lista = [1, 2, 3]
        self.empty_list = []

        # Listy do testów dla merge_data
        self.lista1 = [1, 2]
        self.lista2 = [3, 4]
        self.lista3 = [5, 6]

        # Lista do testów dla remove_duplicates
        self.lista_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
        self.empty_list_for_duplicates = []

    def test_add_element(self):
        """Test dodawania elementu do listy"""
        add_element(self.lista, 4)
        self.assertEqual(self.lista, [1, 2, 3, 4])  # Lista powinna zawierać element 4

        add_element(self.empty_list, "a")
        self.assertEqual(self.empty_list, ["a"])  # Pusta lista po dodaniu elementu "a"

    def test_merge_data(self):
        """Test łączenia dwóch list"""
        result = merge_data(self.lista1, self.lista2)
        self.assertEqual(result, [1, 2, 3, 4])  # Powinna powstać lista z połączonymi danymi

        result = merge_data(self.lista2, self.lista3)
        self.assertEqual(result, [3, 4, 5, 6])  # Inny przypadek z różnymi listami

        result = merge_data([], [])
        self.assertEqual(result, [])  # Łączenie dwóch pustych list daje pustą listę

    def test_remove_duplicates(self):
        """Test usuwania duplikatów z listy"""
        result = remove_duplicates(self.lista_with_duplicates)
        self.assertEqual(result, [1, 2, 3, 4, 5])  # Lista bez duplikatów

        result = remove_duplicates(self.empty_list_for_duplicates)
        self.assertEqual(result, [])  # Pusta lista bez duplikatów to wciąż pusta lista

        result = remove_duplicates([5, 5, 5, 5])
        self.assertEqual(result, [5])  # Lista z samymi duplikatami powinna dać jeden element


if __name__ == "__main__":
    unittest.main()
