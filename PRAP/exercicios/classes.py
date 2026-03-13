'''
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 = Carro("peugot","408")
carro2 = Carro("renault","twingo")

print(f'O meu carro é o {carro1.marca} do modelo {carro1.modelo}')
print(f'O meu carro é o {carro2.marca} do modelo {carro2.modelo}')
'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Camiseta", "R$400,00")
produto2 = Produto("Roda", "R$200,00")

print(f'O produto {produto1.nome} custa {produto1.preco}')
print(f'O produto {produto2.nome} custa {produto2.preco}')