""" -*- coding: utf-8 -*-
Números aleatórios """

import random

""" forçar sempre o mesmo número: random. seed()"""

numero = random.randint(0, 10)
print(numero)


""" escolher aleatoriamente a partir de uma lista"""
lista = [6,45,9]
numero = random.choice(lista)
print(numero)

""" Tratamento de exceções 
tratamento para não interromper execução no meio do programa """

a = 2;
b = 0;

try: 
	print(a/b)
except:
	print("Não é permitida divisão por 0.")

print(a/a)

""" Comando imput

raw_input() strings
input() valores numéricos

o Sublime Text não aceita o comando input( ), 
e você receberá uma mensagem como:
"EOFError: EOF when reading a line".
Esse comando só funciona no terminal/cmd. 
"""