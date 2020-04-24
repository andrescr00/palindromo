import unittest
from palindromo import palindromo

class palin_test(unittest.TestCase):
    def test_palin(self):
        self.assertEqual(palindromo('abcdefebas'), 'efe')
        self.assertEqual(palindromo(123456765),'56765')
        self.assertEqual(palindromo('xyz'),'x')


