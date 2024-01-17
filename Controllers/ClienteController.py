import string
from typing import List
import services.database as db;
import models.Cliente as cliente;
import numpy as np
import psycopg2
from psycopg2 import sql

# Assumindo que db é uma instância de conexão criada em algum lugar
# Você precisa garantir que a conexão esteja aberta antes de chamar essas funções

def Incluir(cliente):
    query = """
    INSERT INTO Cliente (cliNome, cliIdade, cliProfissao) 
    VALUES (%s, %s, %s)
    """
    try:
        db.cursor.execute(query, (cliente.nome, cliente.idade, cliente.profissao))
        db.conn.commit()
    except Exception as e:
        db.conn.rollback()
        print(f"Erro ao inserir dados: {e}")

def SelecionarById(id):
    query = "SELECT * FROM CLIENTE WHERE ID = %s"
    db.cursor.execute(query, (id,))
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return costumerList[0] if costumerList else None

def Alterar(cliente):
    print("alterando...")
    query = """
    UPDATE Cliente
    SET cliNome = %s, cliIdade = %s, cliProfissao = %s
    WHERE id = %s
    """
    db.cursor.execute(query, (cliente.nome, cliente.idade, cliente.profissao, cliente.id))
    db.conn.commit()

def Excluir(id):
    query = "DELETE FROM CLIENTE WHERE id = %s"
    db.cursor.execute(query, (id,))
    db.conn.commit()

def SelecionarTodos():
    query = "SELECT * FROM CLIENTE"
    db.cursor.execute(query)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return costumerList
