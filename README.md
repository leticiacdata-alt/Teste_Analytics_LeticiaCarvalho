# Teste Analytics - Estágio Quod

## Sobre o Projeto
Este repositório contém a resolução do teste técnico para Estágio em Analytics da Quod. O case envolve simulação, limpeza e análise de dados de vendas, além de consultas SQL e relatório de insights.

---

## Como Executar

### Pré-requisitos
- Python 3.8+
- Bibliotecas: pandas, matplotlib

Instale as dependências:
```bash
pip install pandas matplotlib
```

### Passo a Passo

**1. Criar e limpar os dados**
```bash
python scripts/01_limpeza.py
```
Gera os arquivos: `Dados/data_clean.csv` e `Dados/resultados.csv`

**2. Gerar gráficos e análises**
```bash
python scripts/02_graficos.py
```
- Cria os gráficos em `Graficos/`
- Gera o relatório em `Relatorios/relatorio_insights.md`

---

## Estrutura do Projeto
```
Teste_Analytics_SeuNome/
├── scripts/
│   ├── 01_limpeza.py          # Simula e limpa os dados
│   ├── 02_graficos.py         # Cria gráficos e relatório
│   └── consultas_sql.sql       # Consultas SQL do case
├── Dados/
│   ├── data_clean.csv          # Dados após limpeza
│   └── resultados.csv          # Vendas por produto
├── Graficos/
│   ├── vendas_mensais.png      # Gráfico de linha mensal
│   └── vendas_categoria.png    # Gráfico de barras por categoria
├── Relatorios/
│   └── relatorio_insights.md   # Relatório final
└── README.md                    # Este arquivo
```

---

## Consultas SQL
O arquivo `scripts/consultas_sql.sql` contém:
- Listagem de produtos com total de vendas
- Identificação dos produtos com pior desempenho em junho

---

## Suposições Adotadas
- Dados simulados para o ano de 2023
- Produtos baseados no portfólio real da Quod
- Valores faltantes preenchidos com mediana (quantidade) e média (preço)
- Duplicatas removidas
- Linhas sem produto excluídas

---

## Contato
Leticia Carvalho de Sá  
leticiacarvalho.data@gmail.com

---

*Repositório criado para processo seletivo de Estágio em Analytics na Quod*
