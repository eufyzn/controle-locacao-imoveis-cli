
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

