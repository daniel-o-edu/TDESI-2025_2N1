class Funcionario:
    def __init__(self, nome, matricula):
        self.nome = nome     
        self.matricula = matricula  

class Vendedor(Funcionario):
    def __init__ (self,nome, matricula, falar):
        super().__init__(nome, matricula)
        self.falar = falar


func1 = Funcionario("Ruan", "1234")
func2 = Vendedor("Ana","4321" ,"Olá Cliente!!!")

print(f"{func1.nome} atua como {func1.matricula}")

print(f"Meu nome é {func2.nome} matricula {func2.matricula} {func2.falar}")
