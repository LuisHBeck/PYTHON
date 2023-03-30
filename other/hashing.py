from random import randint

pass_input = str(input('Input your password>> '))
pass_input2 = str(input('Confirm your password>> '))

pass_ascii = []

random_mult = randint(0, 9)

def hashing(pass_input):
    pass_hash = ''

    for letter in pass_input:
        pass_ascii.append(ord(letter))

    for i, num in enumerate(pass_ascii):
        x = num * random_mult + (i + (num * 3))
        pass_hash += chr(x)
    pass_ascii.clear()
    return pass_hash

def checking_hash(resgistered_pass, tested_pass):
    if tested_pass == resgistered_pass:
        return True
    else:
        return False

registered_pass = hashing(pass_input)
# print(registered_pass)
tested_pass = hashing(pass_input2)
# print(tested_pass)
checked_pass = checking_hash(registered_pass, tested_pass)

print(f'Login has been released? {checked_pass}')


# another code teste

# def hashing(pass_input):
#     pass_hash = ''
# 
#     for letter in pass_input:
#         pass_ascii.append(ord(letter))
# 
#     for i, num in enumerate(pass_ascii):
#         x = str(num * random_mult) + chr(i + 92)
#         pass_hash += x
#     pass_ascii.clear()
#     return pass_hash
