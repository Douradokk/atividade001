import sqlite3 as lite

# CRUD - Create, Read, Update, Delete

# Criando conexão
con = lite.connect("dados.db")

# Inserir informação
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, sobre) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Acessar informações
def mostrar_info():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        return cur.fetchall()  # Retorna diretamente a lista de resultados

# Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome = ?, email = ?, telefone = ?, dia_em = ?, estado = ?, sobre = ? WHERE id = ?"
        cur.execute(query, i)

# Deletar informação
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id = ?"
        cur.execute(query, i)

