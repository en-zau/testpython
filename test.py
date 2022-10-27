import unittest
import main
import datetime
class unitest1:

    def test_hello_matin(self):
        date = datetime.now().replace(hour=11)
        self.assertEqual(main.hello(date), 'Bonjour !')

    def test_hello_midi(self):
        date = datetime.now().replace(hour=13)
        self.assertEqual(main.hello(date), 'Bon app !')

    def test_hello_aprem(self):
        date = datetime.now().replace(hour=15)
        self.assertEqual(main.hello(date), 'Bonjour !')

    def test_hello_soir(self):
        date = datetime.now().replace(hour=20)
        self.assertEqual(main.hello(date), 'Bonsoir !')

    def test_by_matin(self):
        date = datetime.now().replace(hour=11)
        self.assertEqual(main.hello(date), 'Bonne journée !')

    def test_by_midi(self):
        date = datetime.now().replace(hour=13)
        self.assertEqual(main.hello(date), 'Bon app !')

    def test_hello_aprem(self):
        date = datetime.now().replace(hour=15)
        self.assertEqual(main.hello(date), 'Bon aprem !')

    def test_hello_soir(self):
        date = datetime.now().replace(hour=20)
        self.assertEqual(main.hello(date), 'Bonne soirée !')






    if __name__ == '__main__':
        unittest.main()