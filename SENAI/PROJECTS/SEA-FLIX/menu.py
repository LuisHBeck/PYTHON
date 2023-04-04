from random import randint
from create import *
from read import *

def selection_menu():
    '''
    function using inquirer, for user choose the action
    :return:  select
    '''
    import inquirer
    questions = [
        inquirer.List('option_choose',
                      message="Choose your option",
                      choices=['Register User',
                               'List Movies', 'Register Movie',
                               'Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['option_choose']


def firts_menu():
    import inquirer
    questions = [
        inquirer.List('firts_choose',
                      message="Choose your option",
                      choices=['Login', 'Register User', 'Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['firts_choose']


def select_plan():
    import inquirer
    questions = [
        inquirer.List('plan',
                      message="Choose your plan",
                      choices=['Basic', 'Medium', 'Premium'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['plan']


def select_usertype():
    import inquirer
    questions = [
        inquirer.List('user_type',
                      message="Select your user type",
                      choices=['Normal user', 'ADM'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['user_type']


def select_class():
    import inquirer
    questions = [
        inquirer.List('movie_class',
                      message="Select the classification",
                      choices=[0, 10, 12, 14, 16, 18],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['movie_class']


def menu_repeat():
    option_choose = selection_menu()
    action(option_choose)


def menu_repeat2():
    first_choose = firts_menu()
    action(first_choose)


def id_user():
    y = ''
    z = 0
    for c in range(5):
        x = randint(0,9)
        y += str(x)
        z = int(y)
    return z



def action(choose):
    match choose:
        case 'Exit':
            print("SEE YOU NEXT TIME!")

        case 'Login':
            user_name = str(input("What's your nick?>> ")).title().strip()

            while True:
                try:
                    user_ID = int(input(f'Input your ID, {user_name}>> '))
                    break
                except (ValueError):
                    print('Invalid input! Just numbers.')

            id_valid, id_name = user_id_check(user_ID)

            if id_valid:
                print()
                print(f"WELCOME TO SEA-FLIX, {id_name}!")
                menu_repeat()
            else:
                print('You need to resgister yourself!')
                menu_repeat()

        case 'Register User':
            print("Now it's register time!\n")
            user_name = str(input('Input you name>> ')).strip().title()

            while len(user_name) == 0:
                print("Please input a valid name!")
                user_name = str(input('Input you name>> ')).strip().title()
            user['name'] = user_name

            while True:
                try:
                    user_age = int(input('Input your age>> '))
                    break
                except (ValueError):
                    print('Just numbers, please!')
            user['age'] = user_age

            user_email = str(input('Input you E-mail>> ')).strip().lower()

            while len(user_email) == 0:
                print("Please input an valid E-mail!")
                user_email = str(input('Input you E-mail (use g-mail)>> ')).strip().lower()


            while "@gmail.com" not in user_email:
                print("Invali E-mail (use g-mail)!")
                user_email = str(input('Input you E-mail>> ')).strip().lower()

            user['email'] = user_email
            print()

            user['plan'] = select_plan()

            user_type_input = select_usertype()
            user['type'] = user_type_input
            # if user_type_input == 'ADM':
            #     pass_test = int(input('Input the ADM password>> '))
            #     if pass_test == adm_pass:
            #         print("You're a real ADM!")
            #         user['type'] = user_type_input
            #     else:
            #         print("You're not a ADM. You're a Normal User!")
            #         user['type'] = 'Normal User'

            id_user_ = id_user()
            user['id'] = id_user_

            creat_db(user['name'], user['age'], user['email'],
                     user['plan'], user['type'], user['id'])  #inputing data from the db

            print()
            print("Your register is done!!")
            print(f'Your ID for login is *{id_user_}*')
            print()
            for k, v in user.items():
                print(f'{k} = {v}\n')
            menu_repeat()

        case 'Register Movie':
            movie_title = input('Input the movie title>> ').strip().title()
            movie_desc = input('Input a short description>> ').strip()
            movie_plan = select_plan()
            movie_class = select_class()

            try:
                creat_filmes(movie_title, movie_desc, movie_plan, movie_class)
                print('Successfully registered')
                menu_repeat()
            except:
                print('ERROR WHILE REGISTERING! Try again')
                menu_repeat()

        case 'List Movies':
            show_movies()


user = {}
users = ['2323']
adm_pass = 696969

print("WELCOME TO SEA-FLIX")
menu_repeat2()

x = input()
