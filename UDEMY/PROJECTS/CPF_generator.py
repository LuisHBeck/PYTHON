from random import randint
nove_digitos = ''
for c in range(0, 9):
    nove_digitos += str((randint(0, 9)))

multiplicador1 = 10
multiplciador2 = 11
soma1 = soma2 = 0

for digito in nove_digitos:
    soma1 += (int(digito) * multiplicador1)
    multiplicador1 -= 1

resultado1 = ((soma1 * 10) % 11)
primeiro_digito = 0 if resultado1 > 9 else resultado1

dez_digitos = nove_digitos + str(primeiro_digito)

for digito in dez_digitos:
    soma2 += (int(digito) * multiplciador2)
    multiplciador2 -= 1

resultado2 = ((soma2 * 10) % 11)
segundo_digito = 0 if resultado2 > 9 else resultado2

cpf_resolvido = dez_digitos + str(segundo_digito)


print("GERADOR DE CPF: ")
print("{}.{}.{}-{}".format(cpf_resolvido[:3], cpf_resolvido[3:6], cpf_resolvido[6:9], cpf_resolvido[9:]))

