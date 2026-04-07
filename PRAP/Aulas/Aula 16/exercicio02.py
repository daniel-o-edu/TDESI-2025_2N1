import unittest
import sqlite3

class Usuario:
    def __init__(self, nome, email):
        self.id = None
        self.nome = nome
        self.email = email

class UsuarioDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        
    def salvar(self, usuario):
        cursor = self.conexao.cursor()
        # Execução SQL via substituição de parâmetros
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (usuario.nome, usuario.email))
        self.conexao.commit()
        usuario.id = cursor.lastrowid # Rastreia o ID gerado pelo Banco
        return usuario

    def buscar_por_id(self, id_usuario):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (id_usuario,))
        linha = cursor.fetchone()
        if linha:
            user = Usuario(linha[1], linha[2])
            user.id = linha[0]
            return user
        return None

class TestUsuarioDAO(unittest.TestCase):
    def setUp(self):
        # 1. Abrir conexão e preparar o ambiente
        self.conexao = sqlite3.connect(':memory:')
        self.conexao.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)")
        self.dao = UsuarioDAO(self.conexao)

    def test_salvar_e_buscar_objeto(self):
        # 2. Salvar um objeto (Objeto Python Original)
        usuario_original = Usuario("Ana Silva", "ana@email.com")
        usuario_salvo = self.dao.salvar(usuario_original)
        
        # 3. Buscar o objeto pelo ID
        usuario_recuperado = self.dao.buscar_por_id(usuario_salvo.id)
        
        # 4. Verificar se os dados buscados são iguais aos salvos (Rastreabilidade garantida)
        self.assertIsNotNone(usuario_recuperado)
        self.assertEqual(usuario_original.nome, usuario_recuperado.nome)
        self.assertEqual(usuario_original.email, usuario_recuperado.email)

    def tearDown(self):
        self.conexao.close()

if __name__ == '__main__':
    unittest.main()
