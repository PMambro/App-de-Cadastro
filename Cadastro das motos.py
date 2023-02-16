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

# Centralizando a janela na tela

janela.resizable(0,0)
janela.wm_attributes("-topmost",1) # in front of all the window
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
x = int((screen_width / 2) - (500 / 2))
y = int((screen_height / 2) - (500 / 2))
janela.geometry(f"{500}x{555}+{x}+{y}")

# Criando listas e dicionários com as opções de cada item do cadastro

dictionary = {'Honda': ['CG 160 Start', 'CG 160 Fan', 'CG 160 Titan', 'CG 160 Cargo'], 'Yamaha': ['Fazer 250', 'TT-R 230', 'Fazer 150']}

modelos_honda = ['CG 160 Start', 'CG 160 Fan', 'CG 160 Titan', 'CG 160 Cargo']
modelos_yamaha = ['Fazer 250', 'TT-R 230', 'Fazer 150']

marcas = ['Honda', 'Yamaha', 'Kawasaki', 'Suzuki']
modelos = ['CG 160 Start', 'CG 160 Fan', 'CG 160 Titan', 'CG 160 Cargo','Fazer 250', 'TT-R 230', 'Fazer 150']

marca_var = StringVar()
modelo_var = StringVar()

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

# combobox_marcas = ttk.Combobox(values=marcas_modelos)
# combobox_marcas.grid(row=0, column=1, padx=10, pady=10)

def option_changed(event):
    global modelos
    global combobox_modelo
    modelos = dictionary[marca_var.get()]
    combobox_modelo = ttk.OptionMenu(janela, modelo_var, 'Escolha uma modelo', *dictionary[marca_var.get()], direction='right')
    combobox_modelo.grid(row=1, column=1, sticky=W, padx=50, pady=10)


combobox_marcas = ttk.OptionMenu(janela, marca_var, 'Escolha uma marca', *marcas, direction='right',command=option_changed)
combobox_marcas.grid(row=0, column=1, sticky=W, padx=50, pady=10)



janela.mainloop()
