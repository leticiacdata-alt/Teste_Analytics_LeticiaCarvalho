-- ============================================
-- CONSULTAS SQL - CASE QUOD
-- ============================================
/*
NOTA: O case pede análise de junho/2024, mas os dados simulados 
são de 2023. Por isso, usei junho/2023 como referência para 
demonstrar a lógica da consulta. A estrutura é a mesma para 
qualquer ano - bastaria alterar o filtro para 2024.
*/

-- ============================================
-- CONSULTA 1: Vendas totais por produto
-- ============================================
-- Objetivo: Listar produto, categoria e soma total de vendas
-- Ordenar do maior para o menor valor

SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM 
    vendas
GROUP BY 
    Produto, Categoria
ORDER BY 
    Total_Vendas DESC;

/*
EXPLICAÇÃO DA LÓGICA:

1. SELECT: Escolhe as colunas que serão exibidas:
   - Produto: nome do produto
   - Categoria: categoria do produto  
   - SUM(Quantidade * Preco): calcula o valor total de cada venda 
     (quantidade * preço) e soma todas as vendas do mesmo produto

2. FROM vendas: Indica que estamos usando a tabela 'vendas'

3. GROUP BY Produto, Categoria: Agrupa as linhas que têm o mesmo 
   produto e categoria, para que a soma seja feita por produto

4. ORDER BY Total_Vendas DESC: Ordena o resultado do maior 
   total de vendas para o menor (DESC = decrescente)

Esta consulta permite identificar rapidamente quais são os 
produtos mais vendidos da Quod e suas respectivas categorias.
*/

-- ============================================
-- CONSULTA 2: Produtos com menos vendas em junho
-- ============================================
-- Objetivo: Identificar produtos que venderam menos no mês de junho
-- Como os dados simulados são de 2023, usei junho/2023 como referência

SELECT 
    Produto,
    SUM(Quantidade * Preco) AS Vendas_Junho
FROM 
    vendas
WHERE 
    -- Filtra apenas vendas de junho de 2023
    -- A função DATE_FORMAT depende do banco de dados
    -- Esta versão funciona para MySQL:
    DATE_FORMAT(Data, '%Y-%m') = '2023-06'
    
    -- Alternativa para SQLite:
    -- strftime('%Y-%m', Data) = '2023-06'
    
    -- Alternativa mais simples (se Data for texto no formato YYYY-MM-DD):
    -- Data LIKE '2023-06%'
GROUP BY 
    Produto
ORDER BY 
    Vendas_Junho ASC;

/*
EXPLICAÇÃO DA LÓGICA:

1. WHERE: Filtra apenas as linhas que atendem à condição
   - DATE_FORMAT(Data, '%Y-%m') = '2023-06' extrai ano-mês da data
     e compara com junho/2023

2. GROUP BY Produto: Agrupa as linhas por produto

3. SUM(Quantidade * Preco): Soma o total de vendas de cada produto
   considerando apenas as vendas de junho

4. ORDER BY Vendas_Junho ASC: Ordena do menor para o maior
   (ASC = crescente), mostrando primeiro os produtos que menos venderam

Esta consulta ajuda a identificar produtos com baixo desempenho
em um período específico, permitindo ações direcionadas de marketing
ou revisão de precificação.
*/

-- ============================================
-- CONSULTA 2 - VERSÃO ALTERNATIVA (mais simples)
-- ============================================
-- Caso a coluna Data esteja no formato de texto 'YYYY-MM-DD'

SELECT 
    Produto,
    SUM(Quantidade * Preco) AS Vendas_Junho
FROM 
    vendas
WHERE 
    Data LIKE '2023-06%'  -- pega tudo que começa com '2023-06'
GROUP BY 
    Produto
ORDER BY 
    Vendas_Junho ASC;

-- ============================================
-- CONSULTA 2 - VERSÃO COM LIMIT (opcional)
-- ============================================
-- Para ver apenas os 5 produtos com pior desempenho

SELECT 
    Produto,
    SUM(Quantidade * Preco) AS Vendas_Junho
FROM 
    vendas
WHERE 
    DATE_FORMAT(Data, '%Y-%m') = '2023-06'
GROUP BY 
    Produto
ORDER BY 
    Vendas_Junho ASC
LIMIT 5;

-- ============================================
-- NOTAS SOBRE OS DADOS
-- ============================================
/*
Os dados utilizados nestas consultas são os mesmos gerados
na Parte 1 do case (Python), disponíveis no arquivo 
dados/dados_limpos.csv. A tabela 'vendas' contém as colunas:
- ID: identificador único da venda
- Data: data da transação
- Produto: nome do produto Quod
- Categoria: categoria do produto (Crédito, Fraude, Cobrança, Dados)
- Quantidade: unidades vendidas
- Preco: preço unitário
- Total: valor total (Quantidade * Preco)

As consultas assumem que os dados estão em um banco MySQL,
mas a lógica SQL é aplicável a qualquer SGBD relacional.
*/