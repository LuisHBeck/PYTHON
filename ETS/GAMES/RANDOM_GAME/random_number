from random import randint
from threading import Timer
import os

collors = {
    'X': '\33[7;32m',
    'Y': '\33[7;35m',
    'Z': '\33[7;34m',
    'N': '\33[7;31m',
    'C': '\33[m'
}

tentativas = 0
num_digitado = 0
diferenca = 0
vida = diferenca + 50
acerto = 0


def temponeg(msg="\nSEU TEMPO ACABOU!!"):
    numpensado()
    print(msg)
    pid = os.getpid()
    os.kill(pid, 0)


def comecar():
    pronto = int(input('[1] PARA COMEÇAR: '))
    print('~~'*15)
    while pronto != 1:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
        pronto = int(input('[1] PARA COMEÇAR: '))
        print('~~' * 15)
    if pronto == 1:
        t = Timer(15.0, temponeg)
        t.start()


def numeroGerado():
    numeroPc = randint(1, 100)
    return numeroPc


def subvida():
    diferenca = abs(valorpc - num_digitado)
    return diferenca


def numrecebido():
    num_recebido = num_digitado
    return num_recebido


def cabecalho():
    print('')
    print('==' * 15, ' REGRAS ', '==' * 15)
    print('''O COMPUTADOR IRÁ PENSAR EM UM NÚMERO DE 1 A 100. 
VOCÊ TEM 3 TENTATIVAS; 30 SEGUNDOS; 50 DE VIDA; 
CADA ERRO SERÁ DESCONTADO A DIFERENÇA EM SUA VIDA. TENTE ADIVINHAR''')
    print('==' * 35)


def vidas():
    print('SUA VIDA = {}{}{}'.format(collors['Y'], vida, collors['C']))


def acertou():
    print('{}PARABÉNS, VOCÊ ACERTOU O NÚMERO!!!{}'.format(collors['Z'], collors['C']))


def errou():
    if acerto == 0:
        print('{}VOCÊ PERDEU, NÃO ACERTOU NADA!{}'.format(collors['N'], collors['C']))


def numpensado():
    print('Número pensado = {}{}{}'.format(collors['X'], valorpc, collors['C']))


def teste_exec():
    global tentativas, num_digitado, testdiferenca, vida
    while tentativas < 3 and numeroGerado() != numrecebido() and vida > 0:
        tentativas += 1
        num_digitado = int(input('Digite sua tentativa: \n'))
        print('~~' * 15)
        testdiferenca = subvida()
        vida -= testdiferenca
        vidas()
        teste_acerto()

def teste_acerto():
    global acerto
    if valorpc == num_digitado:
        acerto +=1
        acertou()
        temponeg("FIM DE JOGO!")



cabecalho()
comecar()
vidas()
valorpc = numeroGerado()
teste_exec()
errou()
temponeg("FIM DE JOGO!")
