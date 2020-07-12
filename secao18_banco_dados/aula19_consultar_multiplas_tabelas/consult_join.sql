-- Consultar com múltiplas tabelas

SELECT *
FROM estado e, cidade c
WHERE e.id = c.estado_id;

SELECT e.nome AS Estado, c.nome AS Cidade, regiao AS Região
FROM estado e, cidade c
WHERE e.id = c.estado_id;

SELECT c.nome AS Cidade, e.nome AS Estado,regiao AS Região
FROM estado e
INNER JOIN cidade c on e.id = c.estado_id;
