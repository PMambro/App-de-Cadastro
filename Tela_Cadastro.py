# from main import janela,screen_height,screen_width
from tkinter import *
from tkinter import ttk

class Tela_Cadastro:

    # Clase que contém todos objetos da tela de cadastro

    button_exit = 0
    
    def __init__(self,janela,canvas):
        
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

        marca_var = StringVar()
        modelo_var = StringVar()
        ano_var = StringVar()
        
            # Labels

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

        def option_changed(event):
            global modelos
            global combobox_modelo
            modelos = dictionary[marca_var.get()]
            combobox_modelo = ttk.OptionMenu(canvas, modelo_var, 'Escolha um modelo', *dictionary[marca_var.get()], style='sty.TMenubutton')
            combobox_modelo.place(relx=0.2,rely=0.35, relwidth=0.2, relheight=0.05)

        # Entradas de dados

        combobox_anos = ttk.OptionMenu(canvas,ano_var, 'Escolha um ano', *lista_ano, style = 'sty.TMenubutton')
        combobox_anos.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.05)
        combobox_marcas = ttk.OptionMenu(canvas, marca_var, 'Escolha uma marca', *marcas, command=option_changed, style='sty.TMenubutton')
        combobox_marcas.place(relx=0.2,rely=0.25, relwidth=0.2, relheight=0.05)

    

        self.button_exit = Button(canvas , text="Voltar",fg="Black")
        self.button_exit.place(relx=0.4,rely=0.8, relwidth=0.2, relheight=0.05)
        
  
        