-- Consultar estado

SELECT * FROM estado;

SELECT nome AS 'Estado', sigla AS 'Sigla'
FROM estado
WHERE regiao = 'Nordeste';

SELECT nome AS 'Estado', regiao As 'Região', populacao AS 'População'
FROM estado
WHERE populacao >= 10
ORDER BY populacao DESC;
