import sqlite3

# 1. FUNÇÃO DE CONFIGURAÇÃO (Criação da Tabela)

def configurar_banco():
    """Cria a tabela de produtos se ela ainda não existir."""
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    try:
        # Criação da tabela com chaves adequadas e tipos de dados
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
            )
        ''')
        conexao.commit()
        # print("✅ Banco de dados e tabela configurados com sucesso.") # Opcional
    except sqlite3.Error as erro:
        print(f"⚠️ Erro ao configurar banco de dados: {erro}")
    finally:
        conexao.close()

# 2. FUNÇÕES DO CRUD (CREATE e READ)

def criar_produto(nome, preco):
    """Insere um novo produto no banco de dados."""
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    try:
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
        conexao.commit()
        
        novo_id = cursor.lastrowid
        print(f"\n✅ Sucesso! Produto '{nome}' cadastrado com o ID {novo_id} (Preço: R$ {preco:.2f}).")
        return novo_id
        
    except sqlite3.Error as erro:
        print(f"\n⚠️ Erro de Banco de Dados ao criar produto: {erro}")
        return None
        
    finally:
        conexao.close()


def listar_produtos():
    """Busca e exibe todos os produtos cadastrados no estoque."""
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    try:
        cursor.execute("SELECT id, nome, preco FROM produtos")
        produtos_encontrados = cursor.fetchall()
        
        if not produtos_encontrados:
            print("\nℹ️ Estoque vazio: Nenhum produto cadastrado no momento.")
            return []
            
        print("\n📋 --- LISTA DE PRODUTOS NO ESTOQUE ---")
        for produto in produtos_encontrados:
            id_prod, nome_prod, preco_prod = produto
            print(f"ID: {id_prod:03d} | Produto: {nome_prod:<20} | Preço: R$ {preco_prod:>7.2f}")
        print("---------------------------------------\n")
        
        return produtos_encontrados
        
    except sqlite3.Error as erro:
        print(f"\n⚠️ Erro de Banco de Dados ao listar produtos: {erro}")
        return []
        
    finally:
        conexao.close()

# 3. INTERAÇÃO COM O USUÁRIO (Inputs)

def menu_interativo():
    """Menu simples para o usuário interagir com o sistema."""
    
    # Garante que a tabela existe antes de começar
    configurar_banco()
    
    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        print("1. Adicionar novo produto")
        print("2. Listar produtos cadastrados")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1/2/3): ")
        
        if opcao == '1':
            nome_input = input("\nDigite o nome do produto: ").strip()
            
            # Validação para não cadastrar produto sem nome
            if not nome_input:
                print("❌ Erro: O nome do produto não pode ficar em branco.")
                continue
                
            preco_input = input("Digite o preço do produto (ex: 199.90): ").strip()
            
            # Tratamento de erro para o preço (troca vírgula por ponto e converte para float)
            try:
                preco_formatado = float(preco_input.replace(',', '.'))
                # Chama a função CREATE passando os dados validados
                criar_produto(nome_input, preco_formatado)
            except ValueError:
                print("❌ Erro: Valor inválido! Certifique-se de digitar apenas números (ex: 50.00).")
                
        elif opcao == '2':
            # Chama a função READ
            listar_produtos()
            
        elif opcao == '3':
            print("\nSaindo do sistema... Até logo!")
            break
            
        else:
            print("\n❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_interativo()
