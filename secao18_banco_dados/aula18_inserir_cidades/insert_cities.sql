-- Inserindo dados na tabela cidade

INSERT INTO cidade
    (nome, area, estado_id)
VALUES
    ('Campinas', 729, 25);

INSERT INTO cidade
    (nome, area, estado_id)
VALUES
    ('Niterói', 133.9, 19);

INSERT INTO cidade
    (nome, area, estado_id)
VALUES
    ('Caruaru', 920.6, (SELECT id FROM estado WHERE sigla = 'PE'));

INSERT INTO cidade
    (nome, area, estado_id)
VALUES
    ('Juazeiro do Norte', 248.2, (SELECT id FROM estado WHERE sigla = 'CE'));
