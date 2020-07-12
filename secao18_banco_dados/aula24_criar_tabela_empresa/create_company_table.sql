-- Criar tabela empresa

CREATE TABLE IF NOT EXISTS  empresa (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cnpj INT UNSIGNED,
    PRIMARY KEY(id),
    UNIQUE KEY(cnpj)
);

-- Criar tabela empresa_unidade (N .. M)

CREATE TABLE IF NOT EXISTS empresa_unidade (
    empresa_id INT UNSIGNED NOT NULL,
    cidade_id INT UNSIGNED NOT NULL,
    sede TINYINT(1) NOT NULL,
    PRIMARY KEY(empresa_id, cidade_id)
);
