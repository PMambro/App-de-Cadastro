from tkinter import *
from tkinter import ttk

class Tela_Cadastro:

    # Clase que contém todos objetos da tela de cadastro

    button_exit = 0

    # Variáveis que vao guardar as entradas
    nome_var = str()
    marca_var = str()
    modelo_var = str()
    ano_var = str()
    km_var = str()
    placa_var = str()
    cor_var = str()
    
    def __init__(self,canvas):
        
        def resize_font(event):

            # Função de resize das fontes conforme o tamanho da tela

            global size
            global font
            size = int(event.width /70) 
            font = ("Helvetica", size)
            label_marca.config(font=font)
            label_modelo.config(font=font)
            label_ano.config(font=font)
            label_km.config(font=font)
            label_placa.config(font=font)
            label_nome.config(font=font)
            
            # Menu de seleção
            style = ttk.Style()
            style.configure('sty.TMenubutton', font=('Helvetica',size), background='#c4c4c4', foreground='black')

        canvas.bind("<Configure>", resize_font)

        # Criando listas e dicionários com as opções de cada item do cadastro

        dictionary = {'Honda': ['CG 160 Start', 'CG 160 Fan', 'CG 160 Titan', 'CG 160 Cargo'], 'Yamaha': ['Fazer 250', 'TT-R 230', 'Fazer 150']}
        modelos_honda = ['CG 160 Start', 'CG 160 Fan', 'CG 160 Titan', 'CG 160 Cargo']
        modelos_yamaha = ['Fazer 250', 'TT-R 230', 'Fazer 150']
        marcas = ['Honda', 'Yamaha', 'Kawasaki', 'Suzuki']
        modelos = ['CG 160 Start', 'CG 160 Fan', 'CG 160 Titan', 'CG 160 Cargo','Fazer 250', 'TT-R 230', 'Fazer 150']
        
        lista_ano = []
        for i in range(2000, 2024):
            lista_ano.append(i)
        
            # Labels

        label_nome = Label(canvas, text='Nome:')
        label_nome.place(relx=0.07,rely=0.1, relwidth=0.15, relheight=0.1)

        label_marca = Label(canvas, text='Marca:')
        label_marca.place(relx=0.07,rely=0.2, relwidth=0.15, relheight=0.1)

        label_modelo = Label(canvas, text='Modelo:')
        label_modelo.place(relx=0.07,rely=0.35, relwidth=0.15, relheight=0.1)

        label_ano = Label(canvas, text='Ano:')
        label_ano.place(relx=0.07,rely=0.5, relwidth=0.15, relheight=0.1)

        label_km = Label(canvas, text='KM Rodados:')
        label_km.place(relx=0.07,rely=0.65, relwidth=0.15, relheight=0.1)

        label_placa = Label(canvas, text='Placa:')
        label_placa.place(relx=0.07,rely=0.8, relwidth=0.15, relheight=0.1)

        # Variáveis que vão guardar as entradas

        self.nome_var = StringVar()
        self.marca_var = StringVar()
        self.modelo_var = StringVar()
        self.ano_var = StringVar()
        self.km_var = StringVar()
        self.placa_var = StringVar()


        def select_modelo(event):
            option_modelo = ttk.OptionMenu(canvas, self.modelo_var, 'Escolha um modelo', *dictionary[self.marca_var.get()], command=select_ano, style='sty.TMenubutton')
            option_modelo.place(relx=0.2,rely=0.375, relwidth=0.2, relheight=0.05)

        def select_ano(event):
            option_anos = ttk.OptionMenu(canvas,self.ano_var, 'Escolha um ano', *lista_ano, command=select_km , style = 'sty.TMenubutton', direction='right')
            option_anos.place(relx=0.2, rely=0.525, relwidth=0.2, relheight=0.05)

        def select_km(event):
            option_km = ttk.Entry(canvas, textvariable = self.km_var , background='#c4c4c4', foreground='black')
            option_km.place(relx=0.201, rely=0.675, relwidth=0.3, relheight=0.05)

            option_placa = ttk.Entry(canvas, textvariable = self.placa_var, background='#c4c4c4', foreground='black')
            option_placa.place(relx=0.2, rely=0.825, relwidth=0.3, relheight=0.05)
        
        # Entradas de dados

        nome = ttk.Entry(canvas, textvariable = self.nome_var , background='#c4c4c4', foreground='black')
        nome.place(relx=0.2, rely=0.125, relwidth=0.5, relheight=0.05)

        option_marcas = ttk.OptionMenu(canvas, self.marca_var, 'Escolha uma marca', *marcas, command=select_modelo, style='sty.TMenubutton')
        option_marcas.place(relx=0.2,rely=0.225, relwidth=0.2, relheight=0.05)

        self.button_exit = Button(canvas , text="Voltar",fg="Black")
        self.button_exit.place(relx=0.5,rely=0.93, relwidth=0.2, relheight=0.05, anchor="center")
        
  
        