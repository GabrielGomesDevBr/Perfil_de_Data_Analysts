#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados: Perfil de Data Analysts

# In[1]:


#importando as bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')


# In[8]:


#importando o arquivo
pd.read_csv('jobs_in_data.csv')


# In[9]:


# alterando o nome do arquivo para mais fácil utilização
df = pd.read_csv('jobs_in_data.csv')


# In[11]:


#verificando as primeiras linhas do data frame para melhor compreensão
df.head()


# In[12]:


#verificando as primeiras linhas do data frame para melhor compreensão
df.tail()


# In[13]:


#verificando todos os nomes das colunas
df.columns


# In[15]:


#fazendo a contagem de linhas e colunas
df.shape


# In[16]:


#verificando se existe valores nulos
df.isnull().sum()


# In[20]:


#verificando os tipos de dados
df.dtypes


# In[21]:


#verificando uma descição mais sucinta
df.describe


# In[22]:


#fazendo a contagem de cada coluna
df.count()


# In[24]:


#verificando estatísticas descritivas do data frame
df.describe()


# # Fazendo as análises 

# In[31]:


# Criando um histograma

plt.figure(figsize=(10, 6)) #formato do gráfico
plt.hist(df['salary'], bins=20, color='blue', edgecolor='black') #histograma com 20 "bins" de tamanho, cor azul, cor de limite preto
plt.title('Distribuição Salarial dos Data Analysts') #título do gráfico
plt.xlabel('Salário (USD)') #legenda eixo "X"
plt.ylabel('Frequência') #legenda eixo "Y" 
plt.grid(True) #Grid para melhor vizualização
plt.show #mostrar o gráfico         


# In[40]:


plt.figure(figsize=(10, 6))

# Criando um scatter plot
plt.scatter(df['experience_level'], df['salary'], color='green', alpha=0.5)

plt.title('Distribuição Salarial por Nível de Experiência')
plt.xlabel('Nível de Experiência')
plt.ylabel('Salário (USD)')
plt.grid(True)
plt.show()


# In[41]:


plt.figure(figsize=(12, 8))

# Boxplot para cada moeda
sns.boxplot(x='salary_currency', y='salary', data=df, palette='viridis')

plt.title('Variação Salarial por Moeda')
plt.xlabel('Moeda')
plt.ylabel('Salário (USD)')
plt.grid(True)
plt.show()


# In[42]:


plt.figure(figsize=(12, 8))

# Boxplot para a relação entre nível de experiência e salário
sns.boxplot(x='experience_level', y='salary', data=df, order=['Entry-level', 'Mid-level', 'Senior'], palette='muted')

plt.title('Relação entre Nível de Experiência e Salário')
plt.xlabel('Nível de Experiência')
plt.ylabel('Salário (USD)')
plt.grid(True)
plt.show()


# In[43]:


plt.figure(figsize=(10, 6))

# Contando o número de ocorrências de cada tipo de emprego
employment_counts = df['employment_type'].value_counts()

# Criando um gráfico de barras
sns.barplot(x=employment_counts.index, y=employment_counts.values, palette='pastel')

plt.title('Tipo de Emprego mais Comum para Data Analysts')
plt.xlabel('Tipo de Emprego')
plt.ylabel('Número de Ocorrências')
plt.grid(axis='y')
plt.show()


# In[44]:


# Calculando as porcentagens de cada tipo de emprego
employment_percentages = df['employment_type'].value_counts(normalize=True) * 100

# Exibindo as porcentagens
print("Distribuição Percentual do Tipo de Emprego para Data Analysts:")
print(employment_percentages)


# In[46]:


plt.figure(figsize=(10, 6))

# Criando um gráfico de barras
sns.barplot(x=df['work_setting'].value_counts().index, y=df['work_setting'].value_counts(normalize=True) * 100, palette='Set2')

plt.title('Distribuição Percentual da Configuração de Trabalho para Data Analysts')
plt.xlabel('Configuração de Trabalho')
plt.ylabel('Porcentagem')
plt.grid(axis='y')
plt.show()


# In[45]:


# Calculando as porcentagens de cada configuração de trabalho
work_setting_percentages = df['work_setting'].value_counts(normalize=True) * 100

# Exibindo as porcentagens
print("Distribuição Percentual da Configuração de Trabalho para Data Analysts:")
print(work_setting_percentages)


# In[48]:


plt.figure(figsize=(12, 8))

# Selecionando os 10 primeiros países
top_10_countries = df['employee_residence'].value_counts().head(10)

# Criando um gráfico de barras
sns.barplot(x=top_10_countries.index, y=top_10_countries.values, palette='viridis')

plt.title('Top 10 Países com Maior Número de Data Analysts')
plt.xlabel('País')
plt.ylabel('Número de Data Analysts')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.grid(axis='y')
plt.show()


# In[49]:


plt.figure(figsize=(12, 8))

# Boxplot para a relação entre o título do trabalho e o salário
sns.boxplot(x='job_title', y='salary', data=df, palette='colorblind')

plt.title('Relação entre Título do Trabalho e Salário para Data Analysts')
plt.xlabel('Título do Trabalho')
plt.ylabel('Salário (USD)')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.grid(axis='y')
plt.show()


# In[50]:


plt.figure(figsize=(14, 8))

# Selecionando os 20 primeiros títulos de trabalho
top_20_job_titles = df['job_title'].value_counts().head(20).index

# Filtrando o DataFrame para incluir apenas os 20 primeiros títulos
df_top_20 = df[df['job_title'].isin(top_20_job_titles)]

# Boxplot para a relação entre o título do trabalho e o salário
sns.boxplot(x='job_title', y='salary', data=df_top_20, palette='colorblind')

plt.title('Top 20 Títulos de Trabalho com Maior Número de Data Analysts')
plt.xlabel('Título do Trabalho')
plt.ylabel('Salário (USD)')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.grid(axis='y')
plt.show()


# In[51]:


plt.figure(figsize=(12, 8))

# Boxplot para a relação entre o tamanho da empresa e o salário
sns.boxplot(x='company_size', y='salary', data=df, palette='Set3')

plt.title('Relação entre Tamanho da Empresa e Salário para Data Analysts')
plt.xlabel('Tamanho da Empresa')
plt.ylabel('Salário (USD)')
plt.grid(axis='y')
plt.show()


# In[52]:


plt.figure(figsize=(10, 6))

# Criando um histograma
plt.hist(df['work_year'], bins=20, color='skyblue', edgecolor='black')  # ajuste o número de bins conforme necessário

plt.title('Distribuição de Anos de Trabalho para Data Analysts')
plt.xlabel('Ano de Trabalho')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


# In[53]:


# Taxa de câmbio para converter para USD (você pode ajustar conforme necessário)
exchange_rate_usd = 1.2  # Exemplo hipotético

# Convertendo os salários para USD
df['salary_usd'] = df['salary'] * exchange_rate_usd

# Exibindo a distribuição de salários em USD
plt.figure(figsize=(10, 6))
plt.hist(df['salary_usd'], bins=20, color='orange', edgecolor='black')
plt.title('Distribuição Salarial em USD para Data Analysts')
plt.xlabel('Salário (USD)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


# In[ ]:




