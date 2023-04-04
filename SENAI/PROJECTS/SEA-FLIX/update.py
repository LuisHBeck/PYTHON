from sql import db_connection

connection = db_connection()

def modify_movie(x, y, z, conexao=connection):
    command = f'UPDATE movies SET {x} = "{y}" WHERE idmovies = {z}'
    cursor = conexao.cursor()
    cursor.execute(command)
    conexao.commit()

# modify_movie("movie_desc", "Isaac the king", 1)


def modify_user(x, y, z, conexao=connection):
    command = f'UPDATE users SET {x} = "{y}" WHERE idUsers = {z}'
    cursor = conexao.cursor()
    cursor.execute(command)
    conexao.commit()
