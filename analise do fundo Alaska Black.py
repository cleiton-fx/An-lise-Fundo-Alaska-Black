#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importanto biblioteca investpt

import investpy as inv


# In[2]:


#importando bibliotecas necessárias
#Seaborn é uma biblioteca de visualização de dados construída sobre matplotlib e intimamente integrada com as estruturas de dados do pandas em Python.
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib
matplotlib.rcParams['figure.figsize'] = (16,8)


# In[3]:


#puxando dados
#Aui nos temos dados de todos os fundos BR

fundos_br = inv.get_funds_list(country = 'Brazil')
fundos_br


# In[4]:


#Verificando quantos fundos
len(fundos_br)


# In[5]:


#Pegando os cinco primeiro fundos
fundos_br[:5]


# In[7]:


#Vamos procurar um fundo
#Vamos olhar para o fundo alaska black

pesq = inv.search_funds(by = 'name', value = 'alaska black')
pesq


# In[8]:


#Para melhor visualização do nome
pesq['name'][0]


# In[9]:


#Vamos analisar os dados desde 1900 até 2021
fundo = 'Alaska Black Fundo De Investimento Em Cotas De Fundos De Investimento Em Ações - Bdr Nível I'
alaska = inv.get_fund_historical_data(fundo, country = 'brazil', from_date = '01/01/1900', to_date = '15/07/2021')
alaska


# In[10]:


#Vamos visualizar graficamente

alaska.plot()


# In[ ]:


#Conclusao, atraves das analises dos dados, nos podemos ver se este fundo esta sendo um 
#fundo rentável ou nao, podemos observar que ao longo de 2016 este fundo vem se desempenhando muito bem
#e seu unico pico de queda em inicio de 2020 foi o fato do coronavirus, fora isto esta excelente.

