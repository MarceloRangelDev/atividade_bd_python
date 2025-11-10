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
cursor.execute('''INSERT INTO livros (titulo, autor, ano, genero, disponivel) VALUES
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia', 1),
('O Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasia', 0),
('A Guerra dos Tronos', 'George R.R. Martin', 1996, 'Fantasia', 1),
('O Código Da Vinci', 'Dan Brown', 2003, 'Suspense', 0),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 'Fantasia', 1)
''')

conn.commit()
conn.close()
