import unittest
from produto import Produto
class TesteProduto(unittest.TestCase):
    def setUp(self):
# Roda antes de cada teste para preparar o terreno
        self.item = Produto("Notebook", 3000.00)

    def test_aplicar_desconto_valido(self):
# 10% de 3000 é 300. Preço final: 2700
        preco_final = self.item.aplicar_desconto(10)
        self.assertEqual(preco_final, 2700.00)

    def test_desconto_invalido_gera_erro(self):
# Garante que a exceção seja levantada se passar 150% de desconto
        with self.assertRaises(ValueError):
            self.item.aplicar_desconto(150)

if __name__ == "__main__":
    unittest.main()