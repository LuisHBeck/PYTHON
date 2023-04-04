from sql import db_connection
from prettytable import PrettyTable

connection = db_connection()


def read_user(conexao=connection):
    command = f'SELECT * FROM users'

    cursor = conexao.cursor()  # allows to execute sql commands
    cursor.execute(command)  # execute the command
    result = cursor.fetchall() #read the database

    return result


def show_users():
    table = PrettyTable()
    table.field_names = ['N', 'NAME', 'AGE', 'E-MAIL', 'PLAN', 'TYPE', 'ID']

    for lines in users:
        table.add_row(lines)
    print(table)


def read_movies(conexao=connection):
    command = f'SELECT * FROM movies'

    cursor = conexao.cursor()  # allows to execute sql commands
    cursor.execute(command)  # execute the command
    result = cursor.fetchall()  # read the database

    return result


def show_movies():
    table = PrettyTable()
    table.field_names = ['N', 'NAME', 'DESCRIPTION', 'PLAN', 'CLASS']

    for lines in movies:
        table.add_row(lines)
    print(table)


def user_id_check(n_id):
    for i in range(len(users)):
        if users[i][6] == n_id:
            return True, users[i][1]
        else:
            return False, "——"


users = read_user()
movies = read_movies()

