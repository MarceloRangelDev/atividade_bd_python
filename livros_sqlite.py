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

