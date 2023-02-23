import sqlite3
import pandas as pd


# Inserir o nome do banco

nome = ''


# Criando o banco de dados para o cadastro

conexao = sqlite3.connect(nome)

c = conexao.cursor()

# Colocar as colunas necessárias 
c.execute(''' CREATE TABLE clientes (
     marca text,
     modelo text,
     ano text,
     km text,
     placa text
     )
 ''')

conexao.commit()
conexao.close()