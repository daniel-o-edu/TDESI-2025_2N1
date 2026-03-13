 # 1. Definindo a Classe Base 
class  Animal:
    def  __init__  (self, nome, idade): 
       self.nome = nome 
       self.idade = idade 

    def  emitir_som  (self): 
 # Método genérico que será sobrescrito 
        print(  f"  {self.nome}  faz um som desconhecido."  ) 

# 2. Definindo as Especializações (Herança) 
class  Cachorro(Animal): 
    def  emitir_som  (self): 
# Sobrescrevendo o comportamento da mãe 
        print(  f"  {self.nome}  (Cachorro) diz: Au Au!"  ) 

class  Gato(Animal): 
    def  emitir_som  (self): 
# Sobrescrevendo o comportamento da mãe 
        print(  f"  {self.nome}  (Gato) diz: Miau!"  ) 


# 3. Lógica de funcionamento principal 
print(  "--- Sistema de Atendimento Pet Shop ---"  ) 
pet1 = Cachorro(  "Rex"  ,  4  ) 
pet2 = Gato(  "Mostarda"  ,  10  ) 
pet3 = Animal(  "Dino"  ,  100000  )  # Animal genérico 
 # Resultado esperado: cada objeto sabe exatamente como se comportar 
pet1.emitir_som()  # Saída: Rex (Cachorro) diz: Au Au! 
pet2.emitir_som()  # Saída: Mingau (Gato) diz: Miau! 
pet3.emitir_som()  # Saída: Dino faz um som desconhecido.