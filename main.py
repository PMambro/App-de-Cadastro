from tkinter import *
from tkinter import ttk
import sqlite3
from Tela_Cadastro import Tela_Cadastro
from Menu import Menu
# from PIL import Image, ImageTk

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


# img = Image.open("img\Corsair_.png")
# photo_img = ImageTk.PhotoImage(img)

def menu():

    # Função que cria a tela de menu em um canvas com base na classe Menu que contém todos objetos

    # Canvas menu
    global canvas
    canvas = Canvas(janela,width=janela.winfo_screenwidth(),height=janela.winfo_screenheight(), bd=0 , highlightbackground='white', highlightthickness=10)
    canvas.pack()

    # canvas.create_image(0, 0, image=photo_img , anchor='nw')

    # Colocando todos objetos do menu na tela
    menu = Menu(canvas)

    # Configurando botões 
    menu.button_cadastro.bind("<Button-1>", to_cadastro)
    menu.button_exit.bind("<Button-1>", exit)

def cadastro():

    # Função que cria a tela de cadastro em um canvas com base na classe Tela_Cadastro que contém todos objetos da tela

    # Canvas do cadastro
    global canvas
    canvas = Canvas(janela,width=janela.winfo_screenwidth(),height=janela.winfo_screenheight(), bd=0 , highlightbackground='white', highlightthickness=10)
    canvas.pack()

    # canvas.create_image(0, 0, image=photo_img , anchor='nw')

    # Colocando todos objetos na tela de cadastro
    cadastro = Tela_Cadastro(canvas)

    # Configurando botões 
    cadastro.button_exit.bind("<Button-1>", to_menu)

def to_cadastro(event):
    canvas.destroy()
    cadastro()

def to_menu(event):
    canvas.destroy()
    menu()

def exit(event):
    janela.destroy()

menu()

janela.mainloop()