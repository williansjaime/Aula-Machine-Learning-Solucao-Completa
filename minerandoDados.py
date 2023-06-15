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
#print(len( Colunas_Numericas ))

# Grid - Gráficos

# Tamanho
Figura, Eixo = plt.subplots( figsize=(20, 30) )

# Cor de fundo
Cor_Fundo = '#f5f5f5'
Figura.set_facecolor( Cor_Fundo )

# Paleta de Cores
Paleta_Cores = sns.color_palette( 'flare', len(Colunas_Numericas) * 2 )

# Titulo
plt.suptitle('Análise das Variaveis Numericas', fontsize=22, color='#404040', fontweight=600 )

# Estrutura
Linhas = 7 # (Todas as infos numericas)
Colunas = 2 #( Boxplot - Distplot)
Posicao = 1 # Posicao inicial do grid

# Loop para plotar os gráficos
for Coluna in Colunas_Numericas:

  # Plot no Grid -- Boxplot
  plt.subplot( Linhas, Colunas, Posicao )

  # Titulo
  plt.title( f'{Coluna}', loc='left', fontsize=14, fontweight=200 )

  # Plot
  sns.boxplot( data=Base_Dados, y=Coluna, showmeans=True, saturation=0.75, 
              linewidth=1, color=Paleta_Cores[Posicao], width=0.25 )

  # Mudar
  Posicao += 1

  # Plot no Grid -- Distplot
  plt.subplot( Linhas, Colunas, Posicao )

  # Titulo
  plt.title( f'{Coluna}', loc='left', fontsize=14, fontweight=200 )

  # Plot
  sns.distplot( Base_Dados[Coluna], color=Paleta_Cores[ Posicao - 1 ] )

  # Mudar
  Posicao += 1

# Ajute de Grid
plt.subplots_adjust( top=0.95, hspace=0.3 )

Base_Dados.loc[Base_Dados['area']<=10000]['area'].describe()

#Investigar valor do condominio
Base_Dados.loc[Base_Dados['hoa (R$)']<=10000 ]['hoa (R$)'].describe()

Base_Dados['hoa (R$)'].sort_values(ascending=False).head(20)

#Pesquisar intens na base
Base_Dados.iloc[ 6979 ]

Base_Dados['rent amount (R$)'].describe()

Base_Dados.loc[Base_Dados['rent amount (R$)'] <=10000]['area'].describe()

#filtar IPTU
Base_Dados['property tax (R$)'].sort_values( ascending=False).head(20)

Base_Dados.iloc[ 6645 ]



# Ajuste das colunas categoricas
Base_Dados['animal'] = Base_Dados['animal'].map( {'acept':1, 'not acept':0} )
Base_Dados['furniture'] = Base_Dados['furniture'].map( {'furnished':1, 'not furnished':0} )

# Filtrar a Cidade de São Paulo
Filtro_SP = Base_Dados.loc[ Base_Dados['city'] == 'São Paulo']

# Verificar
Filtro_SP.head()

# Retirando a Coluna Cidade
Filtro_SP.drop( columns=['city'], inplace=True )

# Separa os dados
Caracteristicas = Filtro_SP.drop( columns=['rent amount (R$)'] )
Previsor = Filtro_SP['rent amount (R$)']

# VErificar
Caracteristicas.shape, Previsor.shape

# Caracterticas
Caracteristicas.head()

# Previsoor
Previsor.head()

# Correlação
Filtro_SP.corr()

# Proxima de 1 - Correlação Possitva [ Ambas Sobem ]
# Proxima de -1 - Correlação Negativa [ Uma sobe outra desce ]

# Yellowbrick
from yellowbrick.features import Rank2D

# Definir o metodo
Correlacao = Rank2D( algoritmo='pearson' )

# Fitar função
Correlacao.fit( Caracteristicas, Previsor )
Correlacao.transform( Caracteristicas )
Correlacao.show();


# Separa os dadoos
from sklearn.model_selection import train_test_split

# Divisão dos dados
x_treino, x_teste, y_treino, y_teste = train_test_split(
    Caracteristicas, Previsor, test_size=0.2, random_state=10
)

print(f'Dados de Treino: { x_treino.shape[0] }')
print(f'Dados de Teste: { x_teste.shape[0] }')

# Features mais relevantes
from sklearn.feature_selection import mutual_info_regression
from sklearn.feature_selection import SelectKBest

# Selecao de features
def Selecao_Features( x_treino, y_treino ):

  # Configurar para selecionar as features
  Selecao = SelectKBest( score_func=mutual_info_regression, k=5 )

  # Fitar o aprendizado
  Selecao.fit( x_treino, y_treino )

  return Selecao

# Aplicar essa função
Scores = Selecao_Features( x_treino, y_treino )

# Analisar
for Posicao, Score in enumerate( Scores.scores_ ):
  print( f' { x_treino.columns[Posicao] } : {Score}' )


# Modelo Random Forest Regresson
from sklearn.ensemble import RandomForestRegressor

# Instanciar
Modelo_Floresta = RandomForestRegressor( max_depth=5 )

# Fitar 
Modelo_Floresta.fit( x_treino, y_treino )

# Avaliar a performance
Previsoes = Modelo_Floresta.predict( x_teste )

# Funcao para avaliar
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

print(f'RMSE: { sqrt(mean_squared_error( y_teste, Previsoes ) ) } ')
print(f'Score: { r2_score( y_teste, Previsoes ) } ')

# Avaliando Yellowbrick
from yellowbrick.regressor import PredictionError

# Instanciar
Modelo = RandomForestRegressor( max_depth=5 )
Erro_Modelo = PredictionError( Modelo )

# Fitar
Erro_Modelo.fit( x_treino, y_treino )
Erro_Modelo.score( x_teste, y_teste )
Erro_Modelo.show();