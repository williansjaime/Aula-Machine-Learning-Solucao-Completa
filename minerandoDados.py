# Libs necessarias
import pandas as pd
import numpy as np

# Lib graficas

import matplotlib.pyplot as plt
import seaborn as sns

# Avisos
import warnings

warnings.filterwarnings('ignore')

# Confiração no pandas
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 100)

# Configuração no Matplotlib
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('seaborn-darkgrid')
#print("Terminou")
# Pergunta em Aberto ...
# Quanto vale o aluguel da sua casa ?
# Lendo os dados
Base_Dados = pd.read_csv('house_data.csv')
# Dimensão
#print(Base_Dados.shape)
# Verificar
#print(Base_Dados.head())
# Removendo colunas
Base_Dados.drop( columns=['fire insurance (R$)', 'total (R$)'], inplace=True )
#print(Base_Dados.shape)
# Campos vazios
#print(Base_Dados.isnull().sum().sort_values( ascending=False ))
# Campos unicos
#print(Base_Dados.nunique())
# Tipos das colunas
#print(Base_Dados.info())
# Tipo de colunas
#print(Base_Dados.dtypes.value_counts())

# Filtrar os tipos de colunas
Colunas_Categoricas = Base_Dados.columns[ Base_Dados.dtypes == object ]
Colunas_Numericas = Base_Dados.columns[ Base_Dados.dtypes != object ]

#print(Colunas_Categoricas, Colunas_Numericas)
# Analise dos campos objetos
Base_Dados['city'].value_counts( normalize=True ) * 100

# Loop
#for Coluna in Colunas_Categoricas:

  # Fazendo a analise
  #Analise = Base_Dados[Coluna].value_counts( normalize=True ) * 100

  # Mostrando
  #print( Coluna, '\n', Analise, '\n')


# Correção nos dados
# Ajustando o Andar
Base_Dados.loc[ Base_Dados['floor'] == '301' ]
Base_Dados.iloc[ 2562, 5 ] = 30

# Ajustar o '-'
Base_Dados['floor'] = Base_Dados['floor'].apply( lambda Registro : 0 if Registro == '-' else Registro )
Base_Dados['floor'] = pd.to_numeric( Base_Dados['floor'] )

# Verificar
#print(Base_Dados.head())

#for Coluna in Colunas_Categoricas:

  # Fazendo a analise
  #Analise = Base_Dados[Coluna].value_counts( normalize=True ) * 100

  # Mostrando
  #print( Coluna, '\n', Analise, '\n')
print(len( Colunas_Numericas ))