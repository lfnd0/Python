-- Explorar tipos de 'JOIN'

SELECT *
FROM cidade;

SELECT *
FROM prefeito;

SELECT *
FROM cidade c
INNER JOIN prefeito p ON c.id=p.cidade_id;

SELECT *
FROM cidade c
LEFT JOIN prefeito p on c.id=p.cidade_id; -- LEFT OUTER JOIN prefeito p on c.id=p.cidade_id;

SELECT *
FROM cidade c
RIGHT JOIN prefeito p on c.id=p.cidade_id; -- RIGHT OUTER JOIN prefeito p on c.id=p.cidade_id;

SELECT *
FROM cidade c
LEFT JOIN prefeito p on c.id=p.cidade_id
UNION
SELECT *
FROM cidade c
RIGHT JOIN prefeito p on c.id=p.cidade_id;
