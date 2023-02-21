from tkinter import *
from tkinter import ttk

class Menu:

    # Clase que contém todos objetos da tela Menu

    # definindo alguns objetos como zero para conseguir alterá-los depois
    titulo = 0
    button_cadastro = 0
    button_exit = 0

    def __init__(self,canvas) :

        def resize_font(event):

            # Função de resize das fontes conforme o tamanho da tela

            global size
            global font
            size = int(event.width / 70) 
            font = ("Helvetica", size)
            self.titulo.config(font=("Helvetica", size*2))
            self.button_cadastro.config(font=("Helvetica", size,'bold'))

        canvas.bind("<Configure>", resize_font)
        
        self.titulo = Label(canvas, text="Cadastro de Motos")
        self.titulo.place(relx=0.5,rely=0.1,relwidth=0.35,relheight=0.1, anchor="center")
    
        self.button_cadastro = Button(canvas , text="Cadastrar",fg="Black")
        self.button_cadastro.place(relx=0.5,rely=0.3,relwidth=0.2,relheight=0.1, anchor="center")

        self.button_exit = Button(canvas , text="Sair",fg="Black")
        self.button_exit.place(relx=0.5,rely=0.93, relwidth=0.2, relheight=0.05, anchor='center')
