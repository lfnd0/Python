-- Inserindo dados na tabela prefeito

INSERT INTO prefeito
    (nome, cidade_id)
VALUES
    ('Rodrigo Neves', 2),
    ('Raquel Lyra', 3),
    ('Zenaldo Coutinho', null);

INSERT INTO prefeito
    (nome, cidade_id)
VALUES
    ('Rafael Grecka', null);

-- FK duplicada
INSERT INTO prefeito
    (nome, cidade_id)
VALUES
    ('Rodrigo Pinheiro', 3);
