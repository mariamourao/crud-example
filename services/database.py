# import pyodbc

# server = 'seuservidor' 
# database = 'seubancodedados' 
# username = 'usuario' 
# password = 'senha' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

import psycopg2

#def connect_to_postgresql():
    # Substitua as informações abaixo com os detalhes do seu banco de dados PostgreSQL
host = 'localhost'  # ou o endereço IP do seu servidor PostgreSQL
database = 'postgres'  # ou o nome do seu banco de dados
user = 'postgres'
password = 'special'

# Conectando ao PostgreSQL
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
cursor = conn.cursor()


