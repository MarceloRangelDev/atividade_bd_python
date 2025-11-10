import sqlite3

# Cria o banco de dados livraria.db
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Verifica se a tabela livros existe, caso não exista ela será criada
cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    autor TEXT,
    ano INTEGER,
    genero TEXT,
    disponivel INTEGER CHECK(disponivel IN (0, 1))
)''')

# Inserir 5 Livros Fictícios
# Adicione pelo menos 5 registros de livros na tabela criada.
# cursor.execute('''INSERT INTO livros (titulo, autor, ano, genero, disponivel) VALUES
# ('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia', 1),
# ('O Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasia', 0),
# ('A Guerra dos Tronos', 'George R.R. Martin', 1996, 'Fantasia', 1),
# ('O Código Da Vinci', 'Dan Brown', 2003, 'Suspense', 0),
# ('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 'Fantasia', 1)
# ''')

# Consultar Livros Disponíveis
# Selecione e exiba todos os livros que estão disponíveis (campo disponivel = 1 ).
cursor.execute('''SELECT * FROM livros WHERE disponivel = 1''')
livros_disponiveis = cursor.fetchall()
for livro in livros_disponiveis:
    print(livro)
print("---Nova tarefa---")
# Atualizar Disponibilidade
# Escolha um livro e atualize sua disponibilidade (de 1 para 0 ou vice-versa).
cursor.execute('''UPDATE livros SET disponivel = 0 WHERE id = 1''')
cursor.execute('''SELECT * FROM livros WHERE id = 1''')
livros_disponiveis = cursor.fetchall()
for livro in livros_disponiveis:
    print(livro)
print("---Nova tarefa---")
# Ordenar Livros por Ano
# Liste os livros ordenados do mais recente para o mais antigo (ordem decrescente por ano).
cursor.execute('''SELECT * FROM livros ORDER BY ano DESC''')
livros_ordenados = cursor.fetchall()
for livro in livros_ordenados:
    print(livro)

print("---Nova tarefa---")
    
# Deletar Livro Antigo
# Delete um livro cujo ano de publicação seja anterior a 1940.
cursor.execute('''SELECT * FROM livros WHERE ano < 1940''')
livros_menores_de_1940 = cursor.fetchall()
for livro in livros_menores_de_1940:
    print(livro)
print("---Antes Delete---")
cursor.execute('''DELETE FROM livros WHERE ano < 1940''')
print("---Pós delete---")
cursor.execute('''SELECT * FROM livros WHERE ano < 1940''')
livros_del_menores_de_1940 = cursor.fetchall()
for livro in livros_del_menores_de_1940:
    print(livro)
print("---Nova tarefa---")

# Criar Tabela Usuario
cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)''')

conn.commit()
conn.close()
