-- Deletar estado

DELETE
FROM estado
WHERE sigla = 'AR';

SELECT *
FROM estado;

DELETE
FROM estado
WHERE id >= 30;
