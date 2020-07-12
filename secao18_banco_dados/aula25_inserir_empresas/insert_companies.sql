-- Inserindo dados na tabela empresa e empresa_unidade (Seção 18 - Aula 226)

ALTER TABLE empresa
MODIFY cnpj VARCHAR(14);

DESC empresa;

INSERT INTO empresa
    (nome, cnpj)
VALUES
    ('Bradesco', 71153725000168),
    ('Vale', 50575036000171),
    ('Cielo', 93708804000120);

INSERT INTO empresa_unidade
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);
