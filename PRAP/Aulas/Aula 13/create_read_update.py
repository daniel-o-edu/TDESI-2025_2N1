import sqlite3

# 1. FUNÇÃO DE CONFIGURAÇÃO (Criação da Tabela)

def configurar_banco():
    """Cria a tabela de produtos se ela ainda não existir."""
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
            )
        ''')
        conexao.commit()
    except sqlite3.Error as erro:
        print(f"⚠️ Erro ao configurar banco de dados: {erro}")
    finally:
        conexao.close()

# 2. FUNÇÕES DO CRUD (CREATE, READ, UPDATE)

def criar_produto(nome, preco):
    """CREATE: Insere um novo produto no banco de dados."""
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
    """READ: Busca e exibe todos os produtos cadastrados no estoque."""
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


def buscar_nome_produto(id_produto):
    """Busca auxiliar: Retorna o nome do produto ou None se não existir."""
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome FROM produtos WHERE id = ?", (id_produto,))
    resultado = cursor.fetchone()
    conexao.close()
    
    if resultado:
        return resultado[0] 
    else:
        return None


def atualizar_preco_produto(id_produto, novo_preco):
    """UPDATE: Atualiza o preço de um produto existente."""
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    try:
        # A validação de segurança dentro da função foi mantida
        cursor.execute("SELECT id, nome FROM produtos WHERE id = ?", (id_produto,))
        produto_encontrado = cursor.fetchone()
        
        if produto_encontrado is None:
            print(f"❌ Erro: Produto com ID {id_produto} não encontrado no sistema.")
            return False
            
        cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (novo_preco, id_produto))
        conexao.commit()
        
        print(f"✅ Sucesso: O preço do produto '{produto_encontrado[1]}' foi atualizado para R$ {novo_preco:.2f}.")
        return True
    except sqlite3.Error as erro:
        print(f"⚠️ Erro de Banco de Dados: {erro}")
        return False
    finally:
        conexao.close()

# 3. INTERAÇÃO COM O USUÁRIO (Menu Principal)

def menu_interativo():
    """Menu simples para o usuário interagir com o sistema."""
    
    configurar_banco()
    
    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        print("1. Adicionar novo produto")
        print("2. Listar produtos cadastrados")
        print("3. Atualizar preço de um produto")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4): ").strip()
        
        if opcao == '1':
            nome_input = input("\nDigite o nome do produto: ").strip()
            if not nome_input:
                print("❌ Erro: O nome do produto não pode ficar em branco.")
                continue
                
            preco_input = input("Digite o preço do produto (ex: 199.90): ").strip()
            try:
                preco_formatado = float(preco_input.replace(',', '.'))
                criar_produto(nome_input, preco_formatado)
            except ValueError:
                print("❌ Erro: Valor inválido! Certifique-se de digitar apenas números (ex: 50.00).")
                
        elif opcao == '2':
            listar_produtos()
            
        elif opcao == '3':
            # Chama a lista para o usuário ver os IDs disponíveis antes de atualizar
            listar_produtos()
            print("\n--- MÓDULO DE ATUALIZAÇÃO DE PREÇOS ---")
            
            # Sub-menu em loop para a atualização
            while True:
                entrada_id = input("\nDigite o ID do produto (ou '0' para voltar ao menu principal): ").strip()
                
                if entrada_id == '0' or entrada_id.lower() == 'sair':
                    print("🔙 Retornando ao menu principal...")
                    break
                
                try:
                    id_digitado = int(entrada_id)
                    nome_do_produto = buscar_nome_produto(id_digitado)
                    
                    if nome_do_produto is None:
                        print(f"❌ Alerta: Produto com ID {id_digitado} não localizado no banco de dados!")
                        continue 
                        
                    print(f"📦 Produto localizado: {nome_do_produto}")
                    preco_texto = input("Digite o novo preço (ex: 199.90): ").replace(',', '.')
                    preco_digitado = float(preco_texto)
                    
                    atualizar_preco_produto(id_digitado, preco_digitado)

                except ValueError:
                    print("❌ Erro: Entrada inválida. Certifique-se de digitar apenas números!")
            
        elif opcao == '4':
            print("\n🚪 Saindo do sistema... Até logo!")
            break
            
        else:
            print("\n❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_interativo()
