-- Atualizar estado

UPDATE estado
SET nome = 'Maranhão'
WHERE sigla = 'MA';

SELECT est.nome
FROM estado est
WHERE sigla = 'MA';

UPDATE estado
SET nome = 'Paraná', populacao = 11.32
WHERE sigla = 'PR';

SELECT est.nome, est.sigla, est.populacao
FROM estado est
WHERE sigla = 'PR';
