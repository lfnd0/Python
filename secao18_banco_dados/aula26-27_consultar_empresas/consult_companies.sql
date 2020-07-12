-- Consultar empresas

SELECT e.nome AS Empresa, c.nome AS Cidade
FROM empresa e, empresa_unidade eu, cidade c
WHERE e.id = eu.empresa_id AND c.id = eu.cidade_id AND sede;
