from random import choice

u_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
          'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

l_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

especial = ['/', '(', ')', '*', '-', '_', '>',
            '<', '@', '!', '#', '$', '%', '&']

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

joining = u_case + l_case + especial + num

len = int(input('Input the password len>> '))

password = ''
for c in range(len):
    x = choice(joining)
    password += x
print(password)

