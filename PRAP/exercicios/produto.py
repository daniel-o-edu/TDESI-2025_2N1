class Produto:
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    def aplicar_desconto(self, percentual):
        if percentual < 0 or percentual > 100:
            # Levantando nossa própria exceção ativamente!
            raise ValueError("O desconto deve estar entre 0 e 100.")
        desconto = self.preco_base * (percentual / 100)
        return self.preco_base - desconto