def selection_menu():
    '''
    function using inquirer, for user choose the action
    :return:  select
    '''
    import inquirer
    questions = [
        inquirer.List('option_choose',
                      message="Choose your option",
                      choices=['Login', 'Register User',
                               'List Movies', 'Register Movie',
                               'Menu', 'Logout'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['option_choose']


def select_plan():
    import inquirer
    questions = [
        inquirer.List('plan',
                      message="Choose your plan",
                      choices=['Basic','Medium', 'Premium'],
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


def menu_repeat():
    option_choose = selection_menu()
    action(option_choose)



def action(option_choose):
    match option_choose:
        case 'Logout':
            print("SEE YOU NEXT TIME!")

        case 'Login':
            user_name = str(input("What's your nick?>> ")).title().strip()

            while True:
                try:
                    user_ID = int(input(f'Input your ID, {user_name}>> '))
                    break
                except (ValueError):
                    print('Invalid input! Just numbers.')

            if user_ID in users:
                print()
                print(f"WELCOME TO SEA-FLIX, {user_name}!")
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
            name.append(user_name)

            while True:
                try:
                    user_age = int(input('Input your age>> '))
                    break
                except (ValueError):
                    print('Just numbers, please!')
            age.append(user_age)

            user_email = str(input('Input you E-mail>> ')).strip().lower()

            while len(user_email) == 0:
                print("Please input an valid E-mail!")
                user_email = str(input('Input you E-mail (use g-mail)>> ')).strip().lower()


            while "@gmail.com" not in user_email:
                print("Invali E-mail (use g-mail)!")
                user_email = str(input('Input you E-mail>> ')).strip().lower()

            email.append(user_email)
            print()

            plan.append(select_plan())

            user_type_input = select_usertype()
            if user_type_input == 'ADM':
                pass_test = int(input('Input the ADM password>> '))
                if pass_test == adm_pass:
                    print("You're a real ADM!")
                    user_type.append(user_type_input)
                else:
                    print("You're not a ADM. You're a Normal User!")
                    user_type.append('Normal User')


users = ['2323']
name = []
age = []
email = []
plan = []
user_type = []
adm_pass = 696969

print("WELCOME TO SEA-FLIX")
menu_repeat()
print(users)
print(name)
print(age)
print(plan)
print(user_type)

x = input()
