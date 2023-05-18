import string
from DadosFumantes import DadosFumantes
from Weights import Weights

def getDataExplore(lista_dados: list, propriety: string, value: any):
    quantity = 0
    for data in lista_dados:
        if (data.get_property(propriety) == value and data.get_property("smoke") == "Yes"):
            quantity = quantity + 1
            
    return quantity
        
def calculate_similarity(listaDados, userData: DadosFumantes, weights: Weights):
    somaPesos = weights.age + weights.gender + weights.marital_status + weights.highest_qualification + weights.nationality + weights.ethnicity + weights.gross_income
    listaSimilarity = []
    for dado in listaDados:
        calcAge = 0
        calcGender = 0
        calcMarital = 0
        calcQualification = 0
        calcNationality = 0
        calcEthnicity = 0
        calcGrossIncome = 0
        
        if dado.age == int(userData.age):
            calcAge = int(weights.age)
        if dado.gender == userData.gender:
            calcGender = int(weights.gender)
        if dado.marital_status == userData.marital_status:
            calcMarital = int(weights.marital_status)
        if dado.highest_qualification == userData.highest_qualification:
            calcQualification = int(weights.highest_qualification)
        if dado.nationality == userData.nationality:
            calcNationality = int(weights.nationality)
        if dado.ethnicity == userData.ethnicity:
            calcEthnicity = int(weights.ethnicity)
        if dado.gross_income == userData.gross_income:
            calcGrossIncome = int(weights.gross_income)
            
        dado.similarity = (calcAge + calcGender + calcMarital + calcQualification + calcNationality + calcEthnicity + calcGrossIncome) * 100 / somaPesos
            
        listaSimilarity.append(dado)
        
    return listaSimilarity