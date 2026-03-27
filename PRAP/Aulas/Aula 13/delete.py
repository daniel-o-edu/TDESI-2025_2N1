import sqlite3

def deletar_produto(id_produto):
    conexao = sqlite3.connect('sistema_estoque.db')
    cursor = conexao.cursor()
    
    try:
        # 1. Validação de Checagem: Mirar antes de atirar
        cursor.execute("SELECT nome FROM produtos WHERE id = ?", (id_produto,))
        produto = cursor.fetchone()
        
        if not produto:
            print(f"❌ Cancelado: Nenhum produto associado ao ID {id_produto}.")
            return False
            
        # 2. Execução da Exclusão com a trava do WHERE
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conexao.commit()
        
        print(f"🗑️ Sucesso: Produto '{produto[0]}' removido de forma definitiva.")
        
    except sqlite3.Error as erro:
        print(f"⚠️ Operação de Exclusão bloqueada. Possível restrição de sistema.\nDetalhes técnicos: {erro}")
        
    finally:
        conexao.close()

# Solicitando a remoção do ID 10
deletar_produto(10)
