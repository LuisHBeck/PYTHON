from sql import db_connection

connection = db_connection()

def creat_db(name, age, email, plan, type, id, conexao=connection):
    command = f'''INSERT INTO users(user_name, user_age, user_email, user_plan, user_type, user_id)
    values
    ('{name}', {age}, '{email}', '{plan}', '{type}', {id})'''

    cursor = conexao.cursor() #allows to execute sql commands
    cursor.execute(command) #execute the command
    conexao.commit() #edit the database (upload the changes)


def creat_filmes(name, description, plan, classification, conexao=connection):
    insert_filmes = f'''INSERT INTO movies(movie_name, movie_desc, movie_plan, movie_class)
        values
        ('{name}', '{description}', '{plan}', {classification})'''

    cursor = conexao.cursor()  # allows to execute sql commands
    cursor.execute(insert_filmes)  # execute the command
    conexao.commit()  # edit the database (upload the changes)

