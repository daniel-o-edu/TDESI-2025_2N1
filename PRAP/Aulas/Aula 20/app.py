import jinja2

# 1. Configurar o ambiente do Jinja2 para carregar templates do diretório atual
loader = jinja2.FileSystemLoader(searchpath="./")
env = jinja2.Environment(loader=loader)

# 2. Carregar o arquivo de template perfil.html
template = env.get_template("perfil.html")

# 3. Definir os dados dinâmicos que queremos passar para o template
# No mundo real, esses dados viriam de um banco de dados ou formulário.
dados_do_perfil = {
    "nome": "Ana Silva",
    "usuario_novo": True,
    "habilidades": [
        "Python",
        "Desenvolvimento Web",
        "Machine Learning",
        "Jinja2 Templates"
    ]
}

# 4. Renderizar o template com os dados
# Isso "combina" perfil.html com o dicionário dados_do_perfil
html_final = template.render(dados_do_perfil)

# 5. Salvar o resultado final em um arquivo HTML puro
with open("saida_perfil.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("Página renderizada com sucesso! Abra 'saida_perfil.html' para ver o resultado.")

