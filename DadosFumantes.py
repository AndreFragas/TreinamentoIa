
class DadosFumantes :
    def __init__(self, Id, gender, age, marital_status, highest_qualification, nationality, ethnicity, gross_income, smoke):
        self.Id = Id
        self.gender = gender
        self.age = age
        self.marital_status = marital_status
        self.highest_qualification = highest_qualification
        self.nationality = nationality
        self.ethnicity = ethnicity
        self.gross_income = gross_income
        self.smoke = smoke
        
    def get_property(self, property_name):
        return getattr(self, property_name)
        
    