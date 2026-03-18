def calcular_total_carrinho(lista_precos):
    total = 0
    for preco in lista_precos:
# IMAGINE UM BREAKPOINT NA LINHA ABAIXO (Uma bolinha vermelha na IDE)
       total = total + preco
    return total

precos = [10.0, 20.0, 5.0]
resultado = calcular_total_carrinho(precos)
print(f"Total: {resultado}")