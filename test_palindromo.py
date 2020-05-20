import unittest
from palindromo import palindromo

class palin_test(unittest.TestCase):
    def test0(self):
        self.assertEqual(palindromo('abcdefebas'), 'efe')
    def test1(self):
        self.assertEqual(palindromo('123456765'),'56765')
    def test2(self):
        self.assertEqual(palindromo('xyz'),'x')
    def test3(self):
        self.assertEqual(palindromo('abcdefghijklmnopq'),'a')#sin palindromo
    def test4(self):
        self.assertEqual(palindromo('7?28?2#1?9?1#2?591!2'),'?2#1?9?1#2?')#con caracteres
    def test6(self):
        self.assertEqual(palindromo('0123456789876543210'),'0123456789876543210')#cadena larga
    def test7(self):
        self.assertEqual(palindromo('s'),'s')
    def test8(self):
        self.assertEqual(palindromo(''),'')#vacia
    def test9(self):
        self.assertEqual(palindromo('asddsa98766789seplmsesmlpes'),'seplmsesmlpes')#mas de un palindromo
    def test10(self):
        self.assertEqual(palindromo('7777777777'),'7777777777')
    def test11(self):
        self.assertEqual(palindromo('asddsaseplmsesmlpes98766789'),'seplmsesmlpes')#mas de un palindromo
    def test12(self):
        self.assertEqual(palindromo('seplmsesmlpesasddsa98766789'),'seplmsesmlpes')#mas de un palindromo
    def test13(self):
        self.assertEqual(palindromo('7?28?591!22#1?9?1#2?'),'2#1?9?1#2')#con caracteres
    def test14(self):
        self.assertIn('41233214',palindromo('412332147285912'))#palindromo sin centro

