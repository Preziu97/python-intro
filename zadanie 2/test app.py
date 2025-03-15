import unittest
from app import sprawdz_email, oblicz_pole_kwadratu, filtruj_i_sortuj, konwertuj_date, sprawdz_palindrom


class TestFunctions(unittest.TestCase):
    def test_sprawdz_email(self):
        self.assertTrue(sprawdz_email("test@example.com"))
        self.assertTrue(sprawdz_email("user.name@domain.co"))
        self.assertFalse(sprawdz_email("testexample.com"))
        self.assertFalse(sprawdz_email("test@com"))
        self.assertFalse(sprawdz_email("test@.com"))

    def test_oblicz_pole_kwadratu(self):
        self.assertEqual(oblicz_pole_kwadratu(4), 16)
        self.assertEqual(oblicz_pole_kwadratu(0), 0)
        self.assertEqual(oblicz_pole_kwadratu(10), 100)
        self.assertEqual(oblicz_pole_kwadratu(-5), 25)
        self.assertEqual(oblicz_pole_kwadratu(1.5), 2.25)

    def test_filtruj_i_sortuj(self):
        self.assertEqual(filtruj_i_sortuj([5, 15, 3, 25, 8]), [15, 25])
        self.assertEqual(filtruj_i_sortuj([12, 7, 19, 10, 25]), [12, 19, 25])
        self.assertEqual(filtruj_i_sortuj([1, 2, 3]), [])
        self.assertEqual(filtruj_i_sortuj([50, 30, 5, 15, 80, 10]), [15, 30, 50, 80])
        self.assertEqual(filtruj_i_sortuj([100, 150, 20, 5, 30]), [20, 30, 100, 150])

    def test_konwertuj_date(self):
        self.assertEqual(konwertuj_date("15-03-2025", "%d-%m-%Y", "%Y/%m/%d"), "2025/03/15")
        self.assertEqual(konwertuj_date("25-12-2024", "%d-%m-%Y", "%Y/%m/%d"), "2024/12/25")
        self.assertEqual(konwertuj_date("01-01-2023", "%d-%m-%Y", "%Y/%m/%d"), "2023/01/01")
        self.assertEqual(konwertuj_date("31-07-2022", "%d-%m-%Y", "%Y/%m/%d"), "2022/07/31")
        self.assertEqual(konwertuj_date("15-08-2025", "%d-%m-%Y", "%Y/%m/%d"), "2025/08/15")
        self.assertIsNone(konwertuj_date("2025/03/15", "%Y-%m-%d", "%d-%m-%Y"))

    def test_sprawdz_palindrom(self):
        self.assertTrue(sprawdz_palindrom("kajak"))
        self.assertTrue(sprawdz_palindrom("A man a plan a canal Panama"))  # Przykład z dużymi literami i spacjami
        self.assertTrue(sprawdz_palindrom("madam"))
        self.assertTrue(sprawdz_palindrom("Was it a car or a cat I saw"))
        self.assertFalse(sprawdz_palindrom("hello"))


if __name__ == "__main__":
    unittest.main()
