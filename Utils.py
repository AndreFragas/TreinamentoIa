import string
from DadosFumantes import DadosFumantes

def getDataExplore(lista_dados: list, propriety: string, value: any):
    quantity = 0
    for data in lista_dados:
        if (data.get_property(propriety) == value and data.get_property("smoke") == "Yes"):
            quantity = quantity + 1
            
    return quantity
        
def calculate_similarity(data: DadosFumantes, userData: DadosFumantes):
    similarity: 0.0
    
    
    return similarity

weights = {
    "age": 0.2,
    "gender": 0.1,
    "marital_status": 0.3,
    "highest_qualification": 0.2,
    "nationality": 0.1,
    "ethnicity": 0.1,
    "gross_income": 0.1,
}