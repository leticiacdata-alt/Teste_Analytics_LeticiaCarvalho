from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# SCRIPT 2: GRAFICOS E ANALISE
# ============================================

print("="*60)
print("SCRIPT 2 - GRAFICOS E ANALISE")
print("="*60)

# ============================================
# CARREGAR DADOS
# ============================================

df = pd.read_csv('Dados/data_clean.csv')
df['Data'] = pd.to_datetime(df['Data']) 
df['Total'] = df['Quantidade'] * df['Preco']

print(f"Dados carregados: {len(df)} vendas")
print(f"Total de vendas: R$ {df['Total'].sum():,.2f}")

# ============================================
# GRAFICO 1: VENDAS POR MES
# ============================================

df['Mes'] = df['Data'].dt.month

vendas_mes = []
for mes in range(1, 13):
    linhas_mes = df[df['Mes'] == mes]
    total = linhas_mes['Total'].sum()
    vendas_mes.append(total)

nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
         'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

plt.figure(figsize=(12, 6))
plt.plot(nomes, vendas_mes, color='blue', marker='o', linewidth=2)
plt.title('Vendas por Mes - 2023', fontsize=16)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.grid(True)

for i in range(len(nomes)):
    plt.text(i, vendas_mes[i] + 50, f'R${vendas_mes[i]:.0f}', ha='center')

plt.savefig('Graficos/vendas_mensais.png')
plt.show()
print("Grafico salvo: Graficos/vendas_mensais.png")

# ============================================
# GRAFICO 2: VENDAS POR CATEGORIA
# ============================================

categorias = df['Categoria'].unique() 
vendas_categ = []

for cat in categorias: 
    linhas = df[df['Categoria'] == cat]
    total = linhas['Total'].sum()
    vendas_categ.append(total)

plt.figure(figsize=(10, 6))
plt.bar(categorias, vendas_categ, color='green', alpha=0.7)
plt.title('Vendas por Categoria', fontsize=16)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45)

for i in range(len(categorias)):
    plt.text(i, vendas_categ[i] + 50, f'R${vendas_categ[i]:.0f}', ha='center')

plt.tight_layout()
plt.savefig('Graficos/vendas_categoria.png')
plt.show()
print("Grafico salvo: Graficos/vendas_categoria.png")

# ============================================
# INSIGHT 1: SAZONALIDADE
# ============================================

print("\n" + "="*60)
print("ANALISE DE INSIGHTS")
print("="*60)

print("-"*40)
print("INSIGHT 1 - SAZONALIDADE")
print("-"*40)

melhor_valor = max(vendas_mes)
melhor_pos = vendas_mes.index(melhor_valor)
melhor_mes = nomes[melhor_pos]

pior_valor = min(vendas_mes)
pior_pos = vendas_mes.index(pior_valor)
pior_mes = nomes[pior_pos]

print(f"\nMes com MAIOR venda: {melhor_mes} = R$ {melhor_valor:,.2f}")
print(f"Mes com MENOR venda: {pior_mes} = R$ {pior_valor:,.2f}")

print("\nInterpretacao:")
print(f"   A queda em {pior_mes} pode ser por causa de sazonalidade (carnaval, ferias).")
print(f"   O pico em {melhor_mes} coincide com datas de maior contratacao de servicos.")

print("\nAcoes sugeridas:")
print(f"   • Criar promocoes em {pior_mes}")
print(f"   • Reforcar equipe em {melhor_mes}")
print("   • Planejar lancamentos para periodos de alta demanda")

# ============================================
# INSIGHT 2: PRODUTOS
# ============================================

print("\n" + "-"*40)
print("INSIGHT 2 - PRODUTOS")
print("-"*40)

df_prod = pd.read_csv('Dados/resultados.csv')
total_geral = df['Total'].sum()

produto_campeao = df_prod.iloc[0]['Produto']
valor_campeao = df_prod.iloc[0]['Total_Vendas']
percentual_campeao = (valor_campeao / total_geral) * 100

print(f"\nProduto CAMPEAO: {produto_campeao}")
print(f"   R$ {valor_campeao:,.2f} - {percentual_campeao:.1f}% do total")

print("\nTop 3 produtos:")
for i in range(3):
    prod = df_prod.iloc[i]['Produto']
    valor = df_prod.iloc[i]['Total_Vendas']
    perc = (valor / total_geral) * 100
    print(f"   {i+1}. {prod}: R$ {valor:,.2f} ({perc:.1f}%)")

print("\nInterpretacao:")
print(f"   {produto_campeao} e o carro-chefe da Quod.")
print("   Produtos com baixa venda podem precisar de revisao.")

print("\nAcoes sugeridas:")
print(f"   • Criar combos com {produto_campeao} + outros servicos")
print("   • Focar marketing nos produtos mais vendidos")
print("   • Investigar por que alguns produtos vendem pouco")

# ============================================
# INSIGHT 3: CATEGORIAS
# ============================================

print("\n" + "-"*40)
print("INSIGHT 3 - CATEGORIAS")
print("-"*40)

# Descobrir categoria campea (jeito simples)
maior = 0
cat_campea = ""
cat_valor = 0
for i in range(len(categorias)):
    if vendas_categ[i] > maior:
        maior = vendas_categ[i]
        cat_campea = categorias[i]
        cat_valor = vendas_categ[i]

# Descobrir segunda colocada
segunda_maior = 0
cat_segunda = ""
cat_segunda_valor = 0
for i in range(len(categorias)):
    if vendas_categ[i] != maior and vendas_categ[i] > segunda_maior:
        segunda_maior = vendas_categ[i]
        cat_segunda = categorias[i]
        cat_segunda_valor = vendas_categ[i]

print(f"\nCategoria campea: {cat_campea} = R$ {cat_valor:,.2f}")
print(f"Segunda colocada: {cat_segunda} = R$ {cat_segunda_valor:,.2f}")

print("\nInterpretacao:")
print("   Credito e Fraude sao os pilares do negocio da Quod.")

print("\nAcoes sugeridas:")
print("   • Treinar equipe para vender tambem as outras categorias")
print("   • Revisar mix de produtos das categorias com menor desempenho")

# ============================================
# RELATORIO FINAL EM .MD
# ============================================

print("\n" + "-"*40)
print("GERANDO RELATORIO EM MARKDOWN")
print("-"*40)

# Calcular diferenca entre meses
if pior_valor > 0:
    diferenca = ((melhor_valor - pior_valor) / pior_valor) * 100
else:
    diferenca = 0

# Data atual
data_atual = datetime.now().strftime("%d/%m/%Y")

# Criar relatorio
relatorio = f"""# Relatorio de Insights - Case Quod

## Resumo Executivo
Esta analise examinou **{len(df)} vendas simuladas** em 2023, com faturamento total de **R$ {total_geral:,.2f}**. Foram identificados padroes de sazonalidade e produtos destaque.

---

## Insight 1: Sazonalidade

**Dados:**
- Mes com MAIOR venda: **{melhor_mes}** (R$ {melhor_valor:,.2f})
- Mes com MENOR venda: **{pior_mes}** (R$ {pior_valor:,.2f})
- Diferenca: **{diferenca:.1f}%** entre eles

**Interpretacao:**
A queda em **{pior_mes}** pode ser por causa de sazonalidade (carnaval, ferias).  
O pico em **{melhor_mes}** coincide com datas de maior contratacao de servicos.

**Acoes:**
- Criar promocoes em {pior_mes}
- Reforcar equipe em {melhor_mes}
- Planejar lancamentos para periodos de alta demanda

---

## Insight 2: Produtos

**Dados:**
- Produto campeao: **{produto_campeao}** (R$ {valor_campeao:,.2f})
- Representa **{percentual_campeao:.1f}%** do total
- Top 3: **{df_prod.iloc[0]['Produto']}**, **{df_prod.iloc[1]['Produto']}**, **{df_prod.iloc[2]['Produto']}**

**Interpretacao:**
{produto_campeao} e o carro-chefe da Quod. Produtos com baixa venda podem precisar de revisao.

**Acoes:**
- Criar combos com {produto_campeao} + outros servicos
- Focar marketing nos produtos mais vendidos
- Investigar por que alguns produtos vendem pouco

---

## Insight 3: Categorias

**Dados:**
- Categoria campea: **{cat_campea}** (R$ {cat_valor:,.2f})
- Segunda colocada: **{cat_segunda}** (R$ {cat_segunda_valor:,.2f})

**Interpretacao:**
Credito e Fraude sao os pilares do negocio da Quod.

**Acoes:**
- Treinar equipe para vender tambem as outras categorias
- Revisar mix de produtos das categorias com menor desempenho

---

## Conclusao
Foco em **{melhor_mes}** e em **{produto_campeao}**. Promocoes em **{pior_mes}** para equilibrar as vendas.

---

*Relatorio gerado em {data_atual} com base nos dados simulados do case*
"""

# Salvar relatorio
with open('Relatorios/relatorio_insights.md', 'w', encoding='utf-8') as f:
    f.write(relatorio)

print("Relatorio salvo: Relatorios/relatorio_insights.md")

# ============================================
# RESUMO FINAL
# ============================================

print("\n" + "="*60)
print("SCRIPT FINALIZADO")
print("="*60)
print(f"Total de vendas: R$ {total_geral:,.2f}")
print(f"Melhor mes: {melhor_mes}")
print(f"Pior mes: {pior_mes}")
print(f"Produto campeao: {produto_campeao}")
print("Arquivos salvos em: Graficos/ e Relatorios/")
print("="*60)