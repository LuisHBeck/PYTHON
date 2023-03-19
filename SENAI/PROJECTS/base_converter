from time import sleep

def decBin():
   dec = int(input('INPUT A DECIMAL NUMBER:'))
   binario = bin(dec).replace('0b', '')
   print('Converting...')
   sleep(2)
   print('The number in binary is: {}'.format(binario))

def decHexa():
   dec = int(input('INPUT A DECIMAL NUMBER:'))
   hexa = hex(dec).replace('0x', '')
   print('Converting...')
   sleep(2)
   print('The number in Hexadecimal is: {}'.format(hexa.upper()))

def binDec():
   binary = str(input('INPUT A BINARY NUMBER: '))
   dec = int(binary, 2)
   print('Converting...')
   sleep(2)
   print('The number in decimal is: {}'.format(dec))

def binHexa():
   binary = str(input('INPUT A BINARY NUMBER: '))
   dec = int(binary, 2)
   hexa = hex(dec).replace('0x', '')
   print('Converting...')
   sleep(2)
   print('The number in Hexadecimal is: {}'.format(hexa.upper()))

print('-=-'*12)
print('MENU DE ESCOLHA')
print('[0] - Finalizar')
print('[1] - Decimal para Binário')
print('[2] - Decimal para Hexadecimal')
print('[3] - Binário para Decimal')
print('[4] - Binário para Hexadecimal')
print('-=-'*12)
escolha = int(input('DIGITE SUA OPÇÃO: '))

if escolha == 1:
   decBin()
elif escolha ==2:
   decHexa()
elif escolha == 3:
   binDec()
elif escolha == 4:
   binHexa()
