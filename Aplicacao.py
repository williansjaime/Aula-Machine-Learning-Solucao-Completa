# Contruir a API --> Flask

import joblib
from flask import Flask, request


#Instanciar o aplicativo
aplicativo = Flask(__name__)

#Carregar Modelo
Modelo = joblib.load("Modelo_Floresta_Aleatorio_v100.pkl")

#Funcao para receber uma informacao
@aplicativo.route('/API_Preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>;', methods=['GET'])
def Funcao_01(area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax):
    #Recebendo os inputs da Api
    Lista = [
        float(area), float(rooms), float(bathroom), float(parking_spaces), 
        float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]

    #Tentar a Previsao
    try:
        #Predict
        Previsao = Modelo.predict(Lista)
        return {'Valor_Aluguel':Previsao}
    except:
        return {'Aviso':'Deu algum erro!'}
    
if __name__ == '__main__':
    aplicativo.run(debug=True)