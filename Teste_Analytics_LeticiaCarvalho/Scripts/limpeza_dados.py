
import pandas as pd
from datetime import datetime, timedelta 
import random 

# ======================================================
#   PARTE 1: Criar dados aleátorios para análise
# ======================================================

nomes_produtos = [
    'Score PF',
    'Score PJ',
    'Cadastro Positivo',
    'Autenticação',
    'Biometria',
    'Consulta CPF',
    'Recuperação',
    'Monitoramento'
]

categorias = [
    'Crédito',
    'Crédito',
    'Crédito',
    'Fraude',
    'Fraude',
    'Dados',
    'Cobrança',
    'Fraude'
]

print(f"Produtos cadastrados: {len(nomes_produtos)}")

# Criação de Dicionários de vendas

lista_datas = []
for i in range(50):
    dias = random.randint(0, 364)
    data_inicio = datetime(2023, 1, 1)
    data_final = data_inicio + timedelta(days=dias)
    data_texto = data_final.strftime('%Y-%m-%d')
    lista_datas.append(data_texto)

todas_vendas = []

for i in range(1, 51): 
    indice = random.randint(0, 7)
    produto_escolhido = nomes_produtos[indice]
    categoria_escolhida = categorias[indice]
    data_escolhida = random.choice(lista_datas)
    quantidade = random.randint(1, 10)
    preco = round(random.uniform(100, 5000), 2)
    
    venda = {
        'ID': i,
        'Data': data_escolhida,
        'Produto': produto_escolhido,
        'Categoria': categoria_escolhida,
        'Quantidade': quantidade,
        'Preco': preco
    }
    
    todas_vendas.append(venda)

df = pd.DataFrame(todas_vendas)
print(f"Tabela criada com {len(df)} vendas)")

# ======================================================
#   PARTE 2: Criar problemas aleátorios para análise
# ======================================================

df.loc[5, 'Quantidade'] = None  # linha 5, quantidade vazia
df.loc[12, 'Preco'] = None      # linha 12, preço vazio
df.loc[25, 'Produto'] = None    # linha 25, produto vazio

# Duplicar as primeiras 4 linhas
linhas_duplicadas = df.head(4).copy()
df = pd.concat([df, linhas_duplicadas])

# Verificação da criação dos problemas para limpeza posterior
print(f"Total de linhas agora: {len(df)}")
print("\nValores vazios por coluna:")
print(df.isnull().sum())

# ======================================================
#   PARTE 3: Limpeza dos dados
# ======================================================

df = df.drop_duplicates() # retira as linhas duplicadas do dataframe

mediana_qtd = df['Quantidade'].median() # Preencher quantidades vazias
df['Quantidade'].fillna(mediana_qtd, inplace=True) # Preencher os vazios com a mediana

media_preco = df['Preco'].mean()
df['Preco'].fillna(media_preco, inplace=True)

df = df.dropna(subset=['Produto']) #Remove linhas sem produto 


df['Total'] = df['Quantidade'] * df['Preco']
produtos_unicos = df['Produto'].unique()

maior_venda = 0
melhor_prod = ""

for prod in produtos_unicos:
    linhas = df[df['Produto'] == prod]
    soma = linhas['Total'].sum()
    print(f"{prod}: R$ {soma:.2f}")
    if soma > maior_venda:
        maior_venda = soma
        melhor_prod = prod

print("\n" + "="*50)
print("PRODUTO CAMPEÃO QUOD")
print("="*50)
print(f"Produto: {melhor_prod}")
print(f"Vendas: R$ {maior_venda:.2f}")


df.to_csv('Dados/data_clean.csv', index=False)

resultados = []
for prod in produtos_unicos:
    linhas = df[df['Produto'] == prod]
    soma = linhas['Total'].sum()
    resultados.append([prod, soma])

df_resultados = pd.DataFrame(resultados, columns=['Produto', 'Total_Vendas'])
df_resultados = df_resultados.sort_values('Total_Vendas', ascending=False)

df_resultados.to_csv('Dados/resultados.csv', index=False)


df = pd.read_csv('Dados/data_clean.csv')
df['Total'] = df['Quantidade'] * df['Preco']
total = df['Total'].sum()

print(f"Total de vendas: R$ {total:,.2f}")