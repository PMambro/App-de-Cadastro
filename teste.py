import tkinter as tk
from tkinter import ttk

root = tk.Tk()

options = ['Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', 'Opção 5', 'Opção 6', 'Opção 7', 'Opção 8', 'Opção 9', 'Opção 10', 'Opção 11', 'Opção 12']

selected_option = tk.StringVar()
selected_option.set(options[0])

def open_listbox():
    listbox.tkraise()
    button.config(text='Fechar', command=close_listbox)

def close_listbox():
    button.config(text='Abrir', command=open_listbox)
    listbox.pack_forget()

frame = ttk.Frame(root, padding=10)
frame.pack()

button = ttk.Button(frame, text='Abrir', command=open_listbox)
button.pack(side='left')

listbox = tk.Listbox(frame, listvariable=selected_option)
listbox.pack(side='left', fill='both')

scrollbar = ttk.Scrollbar(frame, orient='vertical', command=listbox.yview)
scrollbar.pack(side='right', fill='y')

listbox.config(yscrollcommand=scrollbar.set)

for option in options:
    listbox.insert('end', option)

root.mainloop()