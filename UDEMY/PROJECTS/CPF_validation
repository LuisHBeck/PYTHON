import re
import sys

cpf_input = input("Digite o CPF: ")
cpf = re.sub(r'[^0-9]', '', cpf_input)
nove_digitos = cpf[:9]

multiplicador1 = 10
multiplciador2 = 11
soma1 = soma2 = 0

for digito in nove_digitos:
    soma1 += (int(digito) * multiplicador1)
    multiplicador1 -= 1

resultado1 = ((soma1 * 10) % 11)
primeiro_digito = 0 if resultado1 > 9 else resultado1

dez_digitos = cpf[:10]

for digito in dez_digitos:
    soma2 += (int(digito) * multiplciador2)
    multiplciador2 -= 1

resultado2 = ((soma2 * 10) % 11)
segundo_digito = 0 if resultado2 > 9 else resultado2

cpf_resolvido = nove_digitos + str(resultado1) + str(resultado2)

teste_rep = cpf_input[0] * len(cpf)

if teste_rep == cpf_resolvido:
    print("CPF INVÁLIDO!")
    sys.exit()

if str(resultado1) == cpf[-2]:
    if str(resultado2) == cpf[-1]:
        print("CPF VÁLIDO!")
    else:
        print("CPF INVÁLIDO")
        print("O certo seria: {}".format(cpf_resolvido))
else:
    print("CPF INVÁLIDO")
    print("O certo seria: {}".format(cpf_resolvido))
