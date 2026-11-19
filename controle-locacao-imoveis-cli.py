import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Imovel (
id_imovel INTEGER PRIMARY KEY AUTOINCREMENT,
rua TEXT NOT NULL,
bairro TEXT UNIQUE NOT NULL,
numero INTEGER NOT NULL,
Valor_aluguel_base REAL NOT NULL,
status TEXT NOT NULL
)
""")
conexao.commit()
conexao.close()
print("Tabela criada!")
