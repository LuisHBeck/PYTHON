from sql import db_connection

connection = db_connection()

def delet_movie(z, conexao=connection):
    command = f'DELETE FROM movies WHERE idmovies = {z}'
    cursor = conexao.cursor()
    cursor.execute(command)
    conexao.commit()

def delet_user(z, conexao=connection):
    command = f'DELETE FROM users WHERE idUsers = {z}'
    cursor = conexao.cursor()
    cursor.execute(command)
    conexao.commit()

delet_movie(4)