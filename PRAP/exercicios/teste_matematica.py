import unittest
from matematica import calcular_dobro

class TestMatematica(unittest.TestCase):
    
    def test_calcular_dobro_positivo(self):
        self.assertEqual(calcular_dobro(2), 6)
    
    def test_calcular_dobro_negativo(self):
        self.assertEqual(calcular_dobro(-3), -6)

if __name__ == '__main__':
    unittest.main()