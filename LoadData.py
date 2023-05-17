from DadosFumantes import DadosFumantes
import json

#Carrega o DataSet em formato Json

def loadData():
    lista = []
    with open('smokingManipulados.json') as arquivo:
        dados = json.load(arquivo)
    
    for dado in dados:
        dadoPersonalizado  = DadosFumantes(dado["Id"], dado["gender"], dado["age"], dado["marital_status"], dado["highest_qualification"], dado["nationality"], dado["ethnicity"], dado["gross_income"], dado["smoke"])
        lista.append(dadoPersonalizado)
    
    return lista