from typing import List
import services.database as db;
import models.Cliente as cliente;


def incluir(cliente):
    sql = "INSERT INTO clientes (nome, idade, profissao) VALUES (%s, %s, %s)"
    values = (cliente.nome,cliente.idade,cliente.profissao)
    db.cursor.execute(sql, values)
    db.db_connection.commit()

def selecionarById(id):
    sql = (f"SELECT * FROM clientes WHERE id = '{id}'")
    db.cursor.execute(sql)
    listaClientes = []

    for linha in db.cursor:
        listaClientes.append(cliente.Cliente(linha[0], linha[1], linha[2], linha[3]))
        
    return listaClientes[0]

def alterar(cliente):
    print(cliente.id)
    sql = (f"UPDATE clientes SET nome = '{cliente.nome}', idade = '{cliente.idade}', profissao = '{cliente.profissao}' WHERE id = '{cliente.id}'")
    #values = (cliente.nome,cliente.idade,cliente.profissao,cliente.id)
    db.cursor.execute(sql)
    db.db_connection.commit()

def excluir(id):
    sql = (f"DELETE FROM clientes WHERE id = '{id}'")
    db.cursor.execute(sql)
    db.db_connection.commit()

def selecionarTodos():
    sql = "SELECT * FROM clientes"
    db.cursor.execute(sql)
    listaClientes = []

    for linha in db.cursor:
        listaClientes.append(cliente.Cliente(linha[0], linha[1], linha[2], linha[3]))
        
    return listaClientes