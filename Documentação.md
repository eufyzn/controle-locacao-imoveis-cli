
Tabelas do Banco de Dados

Inquilino -  (1:N - Um cliente pode alugar varios imoveis)
-id_inquilino PK (Numero Inteiro)
-nome_completo (Texto)
-cpf (Texto,Unico)
-telefone (Texto)
-email (Texto)

Imovel -  (1:N - Um imovel so pode ter um cliente com contrato ativo mas ja poder ter tido diversos contratos ativos)
-id_imovel PK (Numero Inteiro)
-rua (Texto)
-bairro (Texto)
-numero (Numero Inteiro)
-valor_aluguel_base (Real)
-status (Texto)

Contrato - (N:N - Liga os clientes aos imoveis, permitindo que varios clientes aluguem varios imoveis)
-id_inquilino PK FK (Numero Inteiro)
-id_imovel PK FK (Numero Inteiro)
-data_inicio (Texto)Trocar para data?
-data_fim  (Texto)Trocar para data?
-valor_acordado (Real)
-dia_vencimento (Numero Inteiro)


===== CODIGOS =====

1 Criaçao da primeira tabela

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

2 criaçao da segunda tabela

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

