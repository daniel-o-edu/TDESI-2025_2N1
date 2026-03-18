# A função de negócio (O que o sistema faz)
def calcular_desconto(valor_total, cupom):
    if cupom == "SENAI20":
        return valor_total * 0.80 # 20% de desconto
    return valor_total

# O Teste Unitário (A validação)
def test_calcular_desconto():
    # Prepara os dados
    valor_compra = 100.0
    # Executa a função
    resultado = calcular_desconto(valor_compra, "SENAI20")
    # Valida o resultado esperado
    assert resultado == 81.0, f'Erro: Esperado 80.0, mas retornou {resultado}'
    print("Teste Unitário passou com sucesso!")

test_calcular_desconto()