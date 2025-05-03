import unittest
from calculadora import somar

class TestCalculadora(unittest.TestCase):
    def test_soma_dois_numeros(self):
        self.assertEqual(somar(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
