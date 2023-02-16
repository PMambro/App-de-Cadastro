from tkinter import *
from tkinter import ttk
import sqlite3

# Criar base de dados no sqlite3

# conexao = sqlite3.connect('motos.db')
#
# c = conexao.cursor()
#
# c.execute('''CREATE TABLE motos (
#     marca text,
#     modelo text,
#     ano text,
#     KM text,
#     placa text
#     )
# ''')
#
# conexao.commit()
# conexao.close()

# Criando a janela dando um nome
janela = Tk()
janela.title('Motos')

# Criando listas e dicionários com as opções de cada item do cadastro

modelos_honda = ['CG 160 Start', 'CG 160 Fan', 'CG 160 Titan', 'CG 160 Cargo']
modelos_yamaha = ['Fazer 250', 'TT-R 230', 'Fazer 150']

marcas_modelos = ['Honda', 'Yamaha', 'Kawasaki', 'Suzuki']

option_var = StringVar()

lista_ano = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015']

# Labels

label_marca = Label(janela, text='Marca:')
label_marca.grid(row=0, column=0, padx=10, pady=10)

label_modelo = Label(janela, text='Modelo')
label_modelo.grid(row=1, column=0, padx=10, pady=10)

label_ano = Label(janela, text='Ano')
label_ano.grid(row=2, column=0, padx=10, pady=10)

label_km = Label(janela, text='KM Rodados')
label_km.grid(row=3, column=0, padx=10, pady=10)

label_placa = Label(janela, text='Placa')
label_placa.grid(row=4, column=0, padx=10, pady=10)

# Entradas de dados

combobox_marcas = ttk.Combobox(values=marcas_modelos)
combobox_marcas.grid(row=0, column=1, padx=10, pady=10)

teste_option = ttk.OptionMenu(janela, option_var, *marcas_modelos)
teste_option.grid(row=1, column=1, sticky=W, padx=10, pady=10)












janela.mainloop()
