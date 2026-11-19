import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inquilinos (
id_inquilino INTEGER PRIMARY KEY AUTOINCREMENT,
nome_completo TEXT NOT NULL,
cpf TEXT UNIQUE NOT NULL,
telefone TEXT,
email TEXT
)
""")
conexao.commit()
conexao.close()
print("Tabela criada!")
