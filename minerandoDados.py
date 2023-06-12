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
print("Terminou")
# Pergunta em Aberto ...
# Quanto vale o aluguel da sua casa ?
# Lendo os dados
Base_Dados = pd.read_csv('house_data.csv')
# Dimensão
print(Base_Dados.shape)
# Verificar
print(Base_Dados.head())