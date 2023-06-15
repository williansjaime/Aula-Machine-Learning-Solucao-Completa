# Contruir a API --> Flask
from flask import Flask, request


#Instanciar o aplicativo
aplicativo = Flask(__name__)

#Funcao para receber uma informacao
@aplicativo.route('/API_Preditivo/<Parametro1>', methods=['GET'])
def Funcao_01(Parametro1):
    return {'Retorno':f'{Parametro1}'}

if __name__ == '__main__':
    aplicativo.run(debug=True)