-- Inserir estado com id

INSERT INTO estado
    (id, nome, sigla, regiao, populacao)
VALUES
    (30, 'Arapiraca', 'AR', 'Nordeste', 1.54);

INSERT INTO estado
    (nome, sigla, regiao, populacao)
VALUES
    ('Maceió', 'MC', 'Nordeste', 2.54);

SELECT *
FROM estado;
