import unittest
from app import sprawdz_email, oblicz_pole_kwadratu, filtruj_i_sortuj, konwertuj_date, sprawdz_palindrom


class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Przykładowe dane dla testów
        self.email_valid_1 = "test@example.com"
        self.email_valid_2 = "user.name@domain.co"
        self.email_invalid_1 = "testexample.com"
        self.email_invalid_2 = "test@com"
        self.email_invalid_3 = "test@.com"

        self.square_side_1 = 4
        self.square_side_2 = 0
        self.square_side_3 = 10
        self.square_side_4 = -5
        self.square_side_5 = 1.5

        self.numbers_1 = [5, 15, 3, 25, 8]
        self.numbers_2 = [12, 7, 19, 10, 25]
        self.numbers_3 = [1, 2, 3]
        self.numbers_4 = [50, 30, 5, 15, 80, 10]
        self.numbers_5 = [100, 150, 20, 5, 30]

        self.date_str_1 = "15-03-2025"
        self.date_str_2 = "25-12-2024"
        self.date_str_3 = "01-01-2023"
        self.date_str_4 = "31-07-2022"
        self.date_str_5 = "15-08-2025"
        self.invalid_date_str = "2025/03/15"

        self.palindrome_str_1 = "kajak"
        self.palindrome_str_2 = "A man a plan a canal Panama"
        self.palindrome_str_3 = "madam"
        self.palindrome_str_4 = "Was it a car or a cat I saw"
        self.palindrome_str_5 = "hello"

    def test_sprawdz_email(self):
        # Testujemy poprawne adresy email
        self.assertTrue(sprawdz_email(self.email_valid_1))  # Adres email z domeną .com
        self.assertTrue(sprawdz_email(self.email_valid_2))  # Adres email z nazwą domeny zawierającą kropkę

        # Testujemy błędne adresy email
        self.assertFalse(sprawdz_email(self.email_invalid_1))  # Brak znaku '@'
        self.assertFalse(sprawdz_email(self.email_invalid_2))  # Brak domeny
        self.assertFalse(sprawdz_email(self.email_invalid_3))  # Znak '@' jest, ale brak domeny

    def test_oblicz_pole_kwadratu(self):
        # Testujemy obliczanie pola dla różnych boków kwadratu
        self.assertEqual(oblicz_pole_kwadratu(self.square_side_1), 16)  # Pole dla boku 4
        self.assertEqual(oblicz_pole_kwadratu(self.square_side_2), 0)  # Pole dla boku 0
        self.assertEqual(oblicz_pole_kwadratu(self.square_side_3), 100)  # Pole dla boku 10
        self.assertEqual(oblicz_pole_kwadratu(self.square_side_4),
                         25)  # Pole dla boku -5 (kwadrat liczby ujemnej to liczba dodatnia)
        self.assertEqual(oblicz_pole_kwadratu(self.square_side_5), 2.25)  # Pole dla boku 1.5

    def test_filtruj_i_sortuj(self):
        # Testujemy różne listy liczb i oczekiwane wyniki
        self.assertEqual(filtruj_i_sortuj(self.numbers_1), [15, 25])  # Tylko liczby większe niż 10, posortowane
        self.assertEqual(filtruj_i_sortuj(self.numbers_2), [12, 19, 25])  # Tylko liczby większe niż 10, posortowane
        self.assertEqual(filtruj_i_sortuj(self.numbers_3), [])  # Brak liczb większych niż 10
        self.assertEqual(filtruj_i_sortuj(self.numbers_4), [15, 30, 50, 80])  # Liczby większe niż 10, posortowane
        self.assertEqual(filtruj_i_sortuj(self.numbers_5), [20, 30, 100, 150])  # Liczby większe niż 10, posortowane

    def test_konwertuj_date(self):
        # Testujemy poprawność konwersji dat
        self.assertEqual(konwertuj_date(self.date_str_1, "%d-%m-%Y", "%Y/%m/%d"), "2025/03/15")
        self.assertEqual(konwertuj_date(self.date_str_2, "%d-%m-%Y", "%Y/%m/%d"), "2024/12/25")
        self.assertEqual(konwertuj_date(self.date_str_3, "%d-%m-%Y", "%Y/%m/%d"), "2023/01/01")
        self.assertEqual(konwertuj_date(self.date_str_4, "%d-%m-%Y", "%Y/%m/%d"), "2022/07/31")
        self.assertEqual(konwertuj_date(self.date_str_5, "%d-%m-%Y", "%Y/%m/%d"), "2025/08/15")

        # Testujemy niepoprawny format daty
        self.assertIsNone(konwertuj_date(self.invalid_date_str, "%Y-%m-%d", "%d-%m-%Y"))  # Zły format daty wejściowej

    def test_sprawdz_palindrom(self):
        # Testujemy różne przypadki palindromów
        self.assertTrue(sprawdz_palindrom(self.palindrome_str_1))  # Palindrom: "kajak"
        self.assertTrue(sprawdz_palindrom(self.palindrome_str_2))  # Palindrom z dużymi literami i spacjami
        self.assertTrue(sprawdz_palindrom(self.palindrome_str_3))  # Palindrom: "madam"
        self.assertTrue(sprawdz_palindrom(self.palindrome_str_4))  # Palindrom z dużymi literami i spacjami

        # Testujemy przypadek, który nie jest palindromem
        self.assertFalse(sprawdz_palindrom(self.palindrome_str_5))  # "hello" nie jest palindromem


if __name__ == "__main__":
    unittest.main()
