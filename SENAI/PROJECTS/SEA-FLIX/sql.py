import mysql.connector

# connect to database
def db_connection():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='seaflix',
    )
    return conexao
