-- Consultar estado com agregação

SELECT regiao AS 'Região', SUM(populacao) as 'Total'
FROM estado
GROUP BY regiao
ORDER BY Total desc;

SELECT SUM(populacao) as 'Total'
FROM estado;

SELECT AVG(populacao) as 'Média'
FROM estado;
