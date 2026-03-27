import sqlite3

# 1. FUNÇÃO DE ATUALIZAÇÃO

def atualizar_preco_produto(id_produto, novo_preco):
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    try:
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

# 2. FUNÇÃO DE BUSCA PRÉVIA (Para UX)

def buscar_nome_produto(id_produto):
    """Busca o nome do produto no banco para validar o ID antes de pedir o preço."""
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome FROM produtos WHERE id = ?", (id_produto,))
    resultado = cursor.fetchone()
    conexao.close()
    
    if resultado:
        return resultado[0] 
    else:
        return None

# 3. LOOP INTERATIVO COM OPÇÃO DE SAÍDA

print("\n=== MÓDULO DE ATUALIZAÇÃO DE PREÇOS ===")

while True:
    print("\n" + "-" * 45)
    
    # 1. Pede o ID ou a opção de sair
    entrada_id = input("Digite o ID do produto (ou '0' para sair): ").strip()
    
    # Verifica se o usuário quer sair do loop
    if entrada_id == '0' or entrada_id.lower() == 'sair':
        print("\n🚪 Saindo do módulo de atualização... Até logo!")
        break
    
    try:
        # Tenta converter o ID para número
        id_digitado = int(entrada_id)
        
        # 2. Vai ao banco verificar se o ID existe
        nome_do_produto = buscar_nome_produto(id_digitado)
        
        # 3. Se não existir, alerta o usuário e recomeça o loop (continue)
        if nome_do_produto is None:
            print(f"❌ Alerta: Produto com ID {id_digitado} não localizado no banco de dados!")
            continue 
            
        # 4. Se existir, confirma o nome e pede o preço
        print(f"📦 Produto localizado: {nome_do_produto}")
        preco_texto = input("Digite o novo preço (ex: 199.90): ").replace(',', '.')
        preco_digitado = float(preco_texto)
        
        # 5. Executa a atualização
        atualizar_preco_produto(id_digitado, preco_digitado)

    except ValueError:
        print("❌ Erro: Entrada inválida. Certifique-se de digitar apenas números!")
