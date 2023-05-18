class Weights :
    def __init__(self, gender, age, marital_status, highest_qualification, nationality, ethnicity, gross_income):
        self.gender = gender
        self.age = age
        self.marital_status = marital_status
        self.highest_qualification = highest_qualification
        self.nationality = nationality
        self.ethnicity = ethnicity
        self.gross_income = gross_income
        
    def get_property(self, property_name):
        return getattr(self, property_name)