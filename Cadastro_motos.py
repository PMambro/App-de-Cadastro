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

janela.wm_attributes("-topmost",1) # in front of all the window
# janela.resizable(0,0)
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
screen_x = 800
screen_y = 600
x = int((screen_width / 2) - (screen_x / 2))
y = int((screen_height / 2) - (screen_y / 2))
janela.geometry(f"{screen_x}x{screen_y}+{x}+{y}")

# Canvas

canvas = Canvas(janela,width=screen_width,height=screen_height, bd=0 , highlightbackground='white')
canvas.pack()

# Configurando tamanho do texto

def resize_font(event):
    global size
    global font
    size = int(event.width /70) 
    font = ("Arial", size)
    label_marca.config(font=font)
    label_modelo.config(font=font)
    label_ano.config(font=font)
    label_km.config(font=font)
    label_placa.config(font=font)

    # Menu de seleção

    style = ttk.Style()
    style.configure('sty.TMenubutton', font=('Arial',size), background='white')

canvas.bind("<Configure>", resize_font)

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

label_marca = Label(canvas, text='Marca:')
# label_marca.grid(row=0, column=0, padx=10, pady=10)
label_marca.place(relx=0.07,rely=0.2, relwidth=0.15, relheight=0.1)

label_modelo = Label(canvas, text='Modelo')
# label_modelo.grid(row=1, column=0, padx=10, pady=10)
label_modelo.place(relx=0.07,rely=0.35, relwidth=0.15, relheight=0.1)

label_ano = Label(canvas, text='Ano')
# label_ano.grid(row=2, column=0, padx=10, pady=10)
label_ano.place(relx=0.07,rely=0.5, relwidth=0.15, relheight=0.1)

label_km = Label(canvas, text='KM Rodados')
# label_km.grid(row=3, column=0, padx=10, pady=10)
label_km.place(relx=0.07,rely=0.65, relwidth=0.15, relheight=0.1)

label_placa = Label(canvas, text='Placa')
# label_placa.grid(row=4, column=0, padx=10, pady=10)
label_placa.place(relx=0.07,rely=0.8, relwidth=0.15, relheight=0.1)

# Entradas de dados

def option_changed(event):
    global modelos
    global combobox_modelo
    modelos = dictionary[marca_var.get()]
    combobox_modelo = ttk.OptionMenu(janela, modelo_var, 'Escolha um modelo', *dictionary[marca_var.get()], style='sty.TMenubutton')
    # combobox_modelo.grid(row=1, column=1, sticky=W, padx=50, pady=10)
    combobox_modelo.place(relx=0.2,rely=0.35, relwidth=0.2, relheight=0.1)

combobox_marcas = ttk.OptionMenu(canvas, marca_var, 'Escolha uma marca', *marcas, command=option_changed, style='sty.TMenubutton')
# combobox_marcas.grid(row=0, column=1, sticky=W, padx=50, pady=10)
combobox_marcas.place(relx=0.2,rely=0.2, relwidth=0.2, relheight=0.1)

janela.mainloop()
