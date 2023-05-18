
import tkinter as tk
from tkinter import ttk
from DadosFumantes import DadosFumantes
from Weights import Weights
from Utils import calculate_similarity

def create_table(table_frame, data):
    # Criando a tabela usando um widget Treeview
    table = ttk.Treeview(table_frame)

    # Definindo as colunas da tabela
    table["columns"] = ("Id", "Gender", "Age", "Marital Status", "Highest Qualification", "Nationality", "Ethnicity", "Gross Income", "Smoke", "Similarity")

    # Definindo os cabeçalhos das colunas
    table.heading("Id", text="Id")
    table.heading("Gender", text="Gender")
    table.heading("Age", text="Age")
    table.heading("Marital Status", text="Marital Status")
    table.heading("Highest Qualification", text="Highest Qualification")
    table.heading("Nationality", text="Nationality")
    table.heading("Ethnicity", text="Ethnicity")
    table.heading("Gross Income", text="Gross Income")
    table.heading("Smoke", text="Smoke")
    table.heading("Similarity", text="Similarity")
    
    # Definindo o tamanho das colunas
    table.column("Id", width=50)  # Tamanho em pixels
    table.column("Gender", width="100")  # Tamanho usando uma string
    table.column("Age", width=70)
    table.column("Marital Status", width=120)
    table.column("Highest Qualification", width=150)
    table.column("Nationality", width=100)
    table.column("Ethnicity", width=100)
    table.column("Gross Income", width=120)
    table.column("Smoke", width=70)
    table.column("Similarity", width=100)

    sorted_data = sorted(data, key=lambda item: item.similarity, reverse=True)

    # Inserindo os dados na tabela
    for item in sorted_data:
        table.insert("", tk.END, values=(
            item.Id,
            item.gender,
            item.age,
            item.marital_status,
            item.highest_qualification,
            item.nationality,
            item.ethnicity,
            item.gross_income,
            item.smoke,
            item.similarity
        ))

    # Configurando o layout da tabela
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def interface(lista_dados: list):
    def submit() :
        weights = Weights(
            gender=int(weightsGender.get()),
            age=int(weightsAge.get()),
            marital_status=int(weightsMarital.get()),
            highest_qualification=int(weightsHighest.get()),
            nationality=int(weightsNationality.get()),
            ethnicity=int(weightsEthnicity.get()),
            gross_income=int(weightsGrossIncome.get())
        )
        
        userValue = DadosFumantes(
            Id=9999,
            gender=gender_combobox.get(),
            age=age_entry.get(),
            marital_status=marital_status_combobox.get(),
            highest_qualification=highest_qualification_combobox.get(),
            nationality=nationality_combobox.get(),
            ethnicity=ethnicity_combobox.get(),
            gross_income=gross_income_combobox.get(),
            smoke=smoke_combobox.get(),
            similarity=0
        )
        
        result = calculate_similarity(lista_dados, userValue, weights)   
        # Criando a tabela com os dados da lista
        create_table(table_frame, result)
    
    window = tk.Tk()
    window.title("Entrada de Dados")
    window.geometry("1200x600")

    # Criando o frame superior para os campos de entrada e botões
    input_frame = tk.Frame(window)
    input_frame.pack(side=tk.TOP, padx=10, pady=10)

    # Criando os campos de entrada
    gender_label = tk.Label(input_frame, text="Gender:")
    gender_label.grid(row=0, column=0, sticky=tk.W)
    gender_combobox = ttk.Combobox(input_frame, values=["Male", "Female"])
    gender_combobox.grid(row=0, column=1, padx=5, pady=5)
    weightsGender_label = tk.Label(input_frame, text="Weight Gender:")
    weightsGender_label.grid(row=1, column=0, sticky=tk.W)
    weightsGender = tk.Entry(input_frame)
    weightsGender.insert(tk.END, "1")
    weightsGender.grid(row=1, column=1, padx=5, pady=5)
    

    age_label = tk.Label(input_frame, text="Age:")
    age_label.grid(row=0, column=2, sticky=tk.W)
    age_entry = tk.Entry(input_frame)
    age_entry.grid(row=0, column=3, padx=5, pady=5)
    weightsAge_label = tk.Label(input_frame, text="Weight Age:")
    weightsAge_label.grid(row=1, column=2, sticky=tk.W)
    weightsAge = tk.Entry(input_frame)
    weightsAge.insert(tk.END, "1")
    weightsAge.grid(row=1, column=3, padx=5, pady=5)

    marital_status_label = tk.Label(input_frame, text="Marital Status:")
    marital_status_label.grid(row=0, column=4, sticky=tk.W)
    marital_status_combobox = ttk.Combobox(input_frame, values=["Divorced", "Married", "Separated", "Single", "Widowed"])
    marital_status_combobox.grid(row=0, column=5, padx=5, pady=5)
    weightsMarital_label = tk.Label(input_frame, text="Weight Marital Status:")
    weightsMarital_label.grid(row=1, column=4, sticky=tk.W)
    weightsMarital = tk.Entry(input_frame)
    weightsMarital.insert(tk.END, "1")
    weightsMarital.grid(row=1, column=5, padx=5, pady=5)

    highest_qualification_label = tk.Label(input_frame, text="Highest Qualification:")
    highest_qualification_label.grid(row=0, column=6, sticky=tk.W)
    highest_qualification_combobox = ttk.Combobox(input_frame, values=["Degree", "GCSE/CSE", "GCSE/O Level", "Higher/Sub Degree", "No Qualification", "ONC/BTEC", "Other/Sub Degree"])
    highest_qualification_combobox.grid(row=0, column=7, padx=5, pady=5)
    weightsHighest_label = tk.Label(input_frame, text="Weight Highest Qualification:")
    weightsHighest_label.grid(row=1, column=6, sticky=tk.W)
    weightsHighest = tk.Entry(input_frame)
    weightsHighest.insert(tk.END, "1")
    weightsHighest.grid(row=1, column=7, padx=5, pady=5)

    nationality_label = tk.Label(input_frame, text="Nationality:")
    nationality_label.grid(row=2, column=0, sticky=tk.W)
    nationality_combobox = ttk.Combobox(input_frame, values=["British", "English", "Irish", "Scottish", "Welsh", "Other", "Refused", "Unknown"])
    nationality_combobox.grid(row=2, column=1, padx=5, pady=5)
    weightsNationality_label = tk.Label(input_frame, text="Weight Nationality:")
    weightsNationality_label.grid(row=3, column=0, sticky=tk.W)
    weightsNationality = tk.Entry(input_frame)
    weightsNationality.insert(tk.END, "1")
    weightsNationality.grid(row=3, column=1, padx=5, pady=5)

    ethnicity_label = tk.Label(input_frame, text="Ethnicity:")
    ethnicity_label.grid(row=2, column=2, sticky=tk.W)
    ethnicity_combobox = ttk.Combobox(input_frame, values=["Asian", "Black", "Chinese", "Mixed", "White", "Refused Unknown"])
    ethnicity_combobox.grid(row=2, column=3, padx=5, pady=5)
    weightsEthnicity_label = tk.Label(input_frame, text="Weight Ethnicity:")
    weightsEthnicity_label.grid(row=3, column=2, sticky=tk.W)
    weightsEthnicity = tk.Entry(input_frame)
    weightsEthnicity.insert(tk.END, "1")
    weightsEthnicity.grid(row=3, column=3, padx=5, pady=5)

    gross_income_label = tk.Label(input_frame, text="Gross Income:")
    gross_income_label.grid(row=2, column=4, sticky=tk.W)
    gross_income_combobox = ttk.Combobox(input_frame, values=["Under 2,600", "2,600 to 5,200", "5,200 to 10,400", "10,400 to 15,600", "15,600 to 20,800", "20,800 to 28,600", "28,600 to 36,400", "Above 36,400", "Refused and Unknown"])
    gross_income_combobox.grid(row=2, column=5, padx=5, pady=5)
    weightsGrossIncome_label = tk.Label(input_frame, text="Weight Gross Income:")
    weightsGrossIncome_label.grid(row=3, column=4, sticky=tk.W)
    weightsGrossIncome = tk.Entry(input_frame)
    weightsGrossIncome.insert(tk.END, "1")
    weightsGrossIncome.grid(row=3, column=5, padx=5, pady=5)

    smoke_label = tk.Label(input_frame, text="Smoke:")
    smoke_label.grid(row=2, column=6, sticky=tk.W)
    smoke_combobox = ttk.Combobox(input_frame, values=["YES", "NO"])
    smoke_combobox.grid(row=2, column=7, padx=5, pady=5)

    # Botão de submit
    submit_button = tk.Button(input_frame, text="Submit", command=submit)
    submit_button.grid(row=3, column=7, columnspan=2, padx=5, pady=5)

    table_frame = tk.Frame(window)
    table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    window.mainloop()
    

