# Contruir a API --> Flask

import joblib
import sqlite3
from datetime import datetime
from flask import Flask, request

#Instanciar o aplicativo
aplicativo = Flask(__name__)


#--------CARREGAR O Modelo------
Modelo = joblib.load("Modelo_Floresta_Aleatorio_v100.pkl")

#Funcao para receber uma informacao
@aplicativo.route('/API_Preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])
def Funcao_01(area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax):
    
    # Data e hora de inicio
    Data_Incio = datetime.now()
    
    #Recebendo os inputs da Api
    Lista = [
        float(area), float(rooms), float(bathroom), float(parking_spaces), 
        float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]
    print(Lista)
    #Tentar a Previsao
    try:
        #Predict
        Previsao = Modelo.predict([Lista])
        
        #Inserir o valor da Previsão
        Lista.append(str(Previsao))
        
        #Transformando Lista em string
        Input = ''
        for Valor in Lista:
            Input = Input +';'+ str(Valor)
            

        # Data e hora de Final
        Data_Final = datetime.now()
        Processamento = Data_Final - Data_Incio

        #--------CONEXÃO BANCO DE DADOS--------
        Conexao_Banco = sqlite3.connect("Banco_Dados_API.db")
        Cursor = Conexao_Banco.cursor()
        #Query
        Query_Inserindo_Dados = f'''
            INSERT INTO Log_API (Inputs, Inicio, Fim, Processamento)
            VALUES ('{Input}','{Data_Incio}', '{Data_Final}','{Processamento}')
            '''
        print(Query_Inserindo_Dados)
        #Executar a Query
        Cursor.execute(Query_Inserindo_Dados)
        Conexao_Banco.commit()
        Cursor.close()

        return {'Valor_Aluguel':str(Previsao)}
    except:
        return {'Aviso':'Deu algum erro!'}
    
if __name__ == '__main__':
    aplicativo.run(debug=True)