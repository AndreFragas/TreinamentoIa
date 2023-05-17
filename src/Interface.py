
import tkinter as tk
from tkinter import ttk

def interface():
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

    age_label = tk.Label(input_frame, text="Age:")
    age_label.grid(row=0, column=2, sticky=tk.W)
    age_entry = tk.Entry(input_frame)
    age_entry.grid(row=0, column=3, padx=5, pady=5)

    marital_status_label = tk.Label(input_frame, text="Marital Status:")
    marital_status_label.grid(row=0, column=4, sticky=tk.W)
    marital_status_combobox = ttk.Combobox(input_frame, values=["Divorced", "Married", "Separated", "Single", "Widowed"])
    marital_status_combobox.grid(row=0, column=5, padx=5, pady=5)

    highest_qualification_label = tk.Label(input_frame, text="Highest Qualification:")
    highest_qualification_label.grid(row=0, column=6, sticky=tk.W)
    highest_qualification_combobox = ttk.Combobox(input_frame, values=["Degree", "GCSE/CSE", "GCSE/O Level", "Higher/Sub Degree", "No Qualification", "ONC/BTEC", "Other/Sub Degree"])
    highest_qualification_combobox.grid(row=0, column=7, padx=5, pady=5)

    nationality_label = tk.Label(input_frame, text="Nationality:")
    nationality_label.grid(row=1, column=0, sticky=tk.W)
    nationality_combobox = ttk.Combobox(input_frame, values=["British", "English", "Irish", "Scottish", "Welsh", "Other", "Refused", "Unknown"])
    nationality_combobox.grid(row=1, column=1, padx=5, pady=5)

    ethnicity_label = tk.Label(input_frame, text="Ethnicity:")
    ethnicity_label.grid(row=1, column=2, sticky=tk.W)
    ethnicity_combobox = ttk.Combobox(input_frame, values=["Asian", "Black", "Chinese", "Mixed", "White", "Refused Unknown"])
    ethnicity_combobox.grid(row=1, column=3, padx=5, pady=5)

    gross_income_label = tk.Label(input_frame, text="Gross Income:")
    gross_income_label.grid(row=1, column=4, sticky=tk.W)
    gross_income_combobox = ttk.Combobox(input_frame, values=["Under 2,600", "2,600 to 5,200", "5,200 to 10,400", "10,400 to 15,600", "15,600 to 20,800", "20,800 to 28,600", "28,600 to 36,400", "Above 36,400", "Refused and Unknown"])
    gross_income_combobox.grid(row=1, column=5, padx=5, pady=5)

    smoke_label = tk.Label(input_frame, text="Smoke:")
    smoke_label.grid(row=1, column=6, sticky=tk.W)
    smoke_combobox = ttk.Combobox(input_frame, values=["YES", "NO"])
    smoke_combobox.grid(row=1, column=7, padx=5, pady=5)

    # Botão de submit
    submit_button = tk.Button(input_frame, text="Submit", command=submit)
    submit_button.grid(row=2, column=7, columnspan=2, padx=5, pady=5)

    # Criando o frame inferior para exibir a tabela
    # table_frame = tk.Frame(window)
    # table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    window.mainloop()
    
    def submit() :
        # gender = gender_combobox.get()
        # age = age_entry.get()
        # marital_status = marital_status_combobox.get()
        # highest_qualification = highest_qualification_combobox.get()
        # nationality = nationality_combobox.get()
        # ethnicity = ethnicity_combobox.get()
        # gross_income = gross_income_combobox.get()
        # smoke = smoke_combobox.get()
        return