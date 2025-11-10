import sqlite3

# Cria o banco de dados livraria.db
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()