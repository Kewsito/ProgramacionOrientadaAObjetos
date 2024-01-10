import unittest
from ClasePalindromo import Palindromo


class TestPalindromo(unittest.TestCase):
    __palindromo: Palindromo

    def SetUP(self):
        self.__palindromo = Palindromo("anana")

    def test_espalindromo(self):
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_con_un_caract(self):
        self.__palindromo.setPalabra("a")
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra("#")
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra("🖖")
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_con_dos_caract(self):
        self.__palindromo.setPalabra("ab")
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra("ba")
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra("bb")
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra("🖖🖖")
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_con_tres_caract(self):
        self.__palindromo.setPalabra("aba")
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra("bab")
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra("🖖🖖🖖")
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_con_cuatro_caract(self):
        self.__palindromo.setPalabra("baba")
        self.assertTrue(self.__palindromo.esPalindromo())
        self.__palindromo.setPalabra("abab")
        self.assertTrue(self.__palindromo.esPalindromo())


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
