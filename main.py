from Interface import interface
from LoadData import loadData

userValue = None

def main():
    lista_dados = loadData()
    interface(lista_dados)
    
    # quantity_smoker = getDataExplore(lista_dados, 'smoke', 'Yes')
    # #Gender
    # quantity_smoker_male = getDataExplore(lista_dados, 'gender', 'Male')
    # quantity_smoker_female = getDataExplore(lista_dados, 'gender', 'Female')
    # #Marital
    # quantity_smoker_marital_status_divorced = getDataExplore(lista_dados, 'marital_status', 'Divorced')
    # quantity_smoker_marital_status_married = getDataExplore(lista_dados, 'marital_status', 'Married')
    # quantity_smoker_marital_status_separated = getDataExplore(lista_dados, 'marital_status', 'Separated')
    # quantity_smoker_marital_status_single = getDataExplore(lista_dados, 'marital_status', 'Single')
    # quantity_smoker_marital_status_widowed = getDataExplore(lista_dados, 'marital_status', 'Widowed')
    # #Highest_Qualification
    # quantity_smoker_highest_qualification_degree = getDataExplore(lista_dados, 'highest_qualification', 'Degree')
    # quantity_smoker_highest_qualification_GCSECSE = getDataExplore(lista_dados, 'highest_qualification', 'GCSE/CSE')
    # quantity_smoker_highest_qualification_GCSE_O_Level = getDataExplore(lista_dados, 'highest_qualification', 'GCSE/O Level')
    # quantity_smoker_highest_qualification_Higher_Sub_Degree = getDataExplore(lista_dados, 'highest_qualification', 'Higher/Sub Degree')
    # quantity_smoker_highest_qualification_No_Qualification = getDataExplore(lista_dados, 'highest_qualification', 'No Qualification')
    # quantity_smoker_highest_qualification_ONC_BTEC = getDataExplore(lista_dados, 'highest_qualification', 'ONC/BTEC')
    # quantity_smoker_highest_qualification_Other_Sub_Degree = getDataExplore(lista_dados, 'highest_qualification', 'Other/Sub Degree')
    # #Nationality
    # quantity_smoker_nationality_British = getDataExplore(lista_dados, 'nationality', 'British')
    # quantity_smoker_nationality_English = getDataExplore(lista_dados, 'nationality', 'English')
    # quantity_smoker_nationality_Irish = getDataExplore(lista_dados, 'nationality', 'Irish')
    # quantity_smoker_nationality_Scottish = getDataExplore(lista_dados, 'nationality', 'Scottish')
    # quantity_smoker_nationality_Welsh = getDataExplore(lista_dados, 'nationality', 'Welsh')
    # quantity_smoker_nationality_Other = getDataExplore(lista_dados, 'nationality', 'Other')
    # quantity_smoker_nationality_Refused = getDataExplore(lista_dados, 'nationality', 'Refused')
    # quantity_smoker_nationality_Unknown = getDataExplore(lista_dados, 'nationality', 'Unknown')
    # #Ethnicity
    # quantity_smoker_ethnicity_Asian = getDataExplore(lista_dados, 'ethnicity', 'Asian')
    # quantity_smoker_ethnicity_Black = getDataExplore(lista_dados, 'ethnicity', 'Black')
    # quantity_smoker_ethnicity_Chinese = getDataExplore(lista_dados, 'ethnicity', 'Chinese')
    # quantity_smoker_ethnicity_Mixed = getDataExplore(lista_dados, 'ethnicity', 'Mixed')
    # quantity_smoker_ethnicity_White = getDataExplore(lista_dados, 'ethnicity', 'White')
    # quantity_smoker_ethnicity_Refused_Unknown = getDataExplore(lista_dados, 'ethnicity', 'Refused Unknown')
    # #Gross Income
    # quantity_smoker_gross_income_Under_2600 = getDataExplore(lista_dados, 'gross_income', 'Under 2,600')
    # quantity_smoker_gross_income_2600_to_5200 = getDataExplore(lista_dados, 'gross_income', '2,600 to 5,200')
    # quantity_smoker_gross_income_5200_to_10400 = getDataExplore(lista_dados, 'gross_income', '5,200 to 10,400')
    # quantity_smoker_gross_income_10400_to_15600 = getDataExplore(lista_dados, 'gross_income', '10,400 to 15,600')
    # quantity_smoker_gross_income_15600_to_20800 = getDataExplore(lista_dados, 'gross_income', '15,600 to 20,800')
    # quantity_smoker_gross_income_20800_to_28600 = getDataExplore(lista_dados, 'gross_income', '20,800 to 28,600')
    # quantity_smoker_gross_income_28600_to_36400 = getDataExplore(lista_dados, 'gross_income', '28,600 to 36,400')
    # quantity_smoker_gross_income_Above_36400 = getDataExplore(lista_dados, 'gross_income', 'Above 36,400')
    # quantity_smoker_gross_income_Refused_and_Unknown = getDataExplore(lista_dados, 'gross_income', 'Refused and Unknown')
    
    # print("Quantidade de Dados: ", len(lista_dados))
    # print('Quantidade Smoker: ', quantity_smoker)
    # #Gender
    # print('Quantidade Male: ', quantity_smoker_male)
    # print('Quantidade Female: ', quantity_smoker_female)
    # #Marital
    # print('Quantidade Divorced: ', quantity_smoker_marital_status_divorced)
    # print('Quantidade Married: ', quantity_smoker_marital_status_married)
    # print('Quantidade Separated: ', quantity_smoker_marital_status_separated)
    # print('Quantidade Single: ', quantity_smoker_marital_status_single)
    # print('Quantidade Widowed: ', quantity_smoker_marital_status_widowed)
    # #Highest_Qualification
    # print('Quantidade Degree: ', quantity_smoker_highest_qualification_degree)
    # print('Quantidade GCSE/CSE: ', quantity_smoker_highest_qualification_GCSECSE)
    # print('Quantidade GCSE/O Level: ', quantity_smoker_highest_qualification_GCSE_O_Level)
    # print('Quantidade Higher/Sub Degree: ', quantity_smoker_highest_qualification_Higher_Sub_Degree)
    # print('Quantidade No Qualification: ', quantity_smoker_highest_qualification_No_Qualification)
    # print('Quantidade ONC/BTEC: ', quantity_smoker_highest_qualification_ONC_BTEC)
    # print('Quantidade Other/Sub Degree: ', quantity_smoker_highest_qualification_Other_Sub_Degree)
    # #Nationality
    # print('Quantidade British: ', quantity_smoker_nationality_British)
    # print('Quantidade English: ', quantity_smoker_nationality_English)
    # print('Quantidade Irish: ', quantity_smoker_nationality_Irish)
    # print('Quantidade Scottish: ', quantity_smoker_nationality_Scottish)
    # print('Quantidade Welsh: ', quantity_smoker_nationality_Welsh)
    # print('Quantidade Other: ', quantity_smoker_nationality_Other)
    # print('Quantidade Refused: ', quantity_smoker_nationality_Refused)
    # print('Quantidade Unknown: ', quantity_smoker_nationality_Unknown)
    # #Ethnicity
    # print('Quantidade Asian: ', quantity_smoker_ethnicity_Asian)
    # print('Quantidade Black: ', quantity_smoker_ethnicity_Black)
    # print('Quantidade Chinese: ', quantity_smoker_ethnicity_Chinese)
    # print('Quantidade Mixed: ', quantity_smoker_ethnicity_Mixed)
    # print('Quantidade White: ', quantity_smoker_ethnicity_White)
    # print('Quantidade Refused Unknown: ', quantity_smoker_ethnicity_Refused_Unknown)
    # #Gross Income
    # print('Quantidade Under 2,600: ', quantity_smoker_gross_income_Under_2600)
    # print('Quantidade 2,600 to 5,200: ', quantity_smoker_gross_income_2600_to_5200)
    # print('Quantidade 5,200 to 10,400: ', quantity_smoker_gross_income_5200_to_10400)
    # print('Quantidade 10,400 to 15,600: ', quantity_smoker_gross_income_10400_to_15600)
    # print('Quantidade 15,600 to 20,800: ', quantity_smoker_gross_income_15600_to_20800)
    # print('Quantidade 20,800 to 28,600: ', quantity_smoker_gross_income_20800_to_28600)
    # print('Quantidade 28,600 to 36,400: ', quantity_smoker_gross_income_28600_to_36400)
    # print('Quantidade Above 36,400: ', quantity_smoker_gross_income_Above_36400)
    # print('Quantidade Refused and Unknown: ', quantity_smoker_gross_income_Refused_and_Unknown)

main()