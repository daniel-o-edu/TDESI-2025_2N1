import unittest

# Simulando um comportamento de DAO para o teste
def verificar_tipo_entrada(idade):
    if not isinstance(idade, int):
        raise TypeError("A idade deve ser um número inteiro.")
    return True

class TesteConfiabilidade(unittest.TestCase):
    def test_falha_tipo_entrada(self):
        # Valida se o DAO levanta TypeError ao receber string em campo numérico
        # self.assertRaises(exceção_esperada, função, argumentos...)
        self.assertRaises(TypeError, verificar_tipo_entrada, 'texto_invalido')

if __name__ == '__main__':
    unittest.main()
