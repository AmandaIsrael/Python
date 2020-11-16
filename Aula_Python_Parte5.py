""" -*- coding: utf-8 -*-

Funções --> declarar funções primeiro
def - palavra reservada

def NOME(PARÂMETROS):
	COMANDOS
Chamada:
NOME(ARGUMENTOS) """

def soma(x, y):
	return(x+y)

def mult(x, y):
	return(x*y)

s = soma(2, 4)
m = mult(3,4)
print(soma(s,m))

""" Arquivo
r - somente leitura
w - escrita (apaga arquivo já existente e cria um novo)
a - leitura e escrita (add ao fim)
r+ - leitura e escrita
w+ - escrita (= w)
a + - leitura e escrita (update)
"""
arquivo = open("arquivo1.txt")

""" read() - lê todo o arquivo
	readline() - lê uma linha
	readlines() - lê arquivo e armazena em uma lista
"""
linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
	print(linha)

w = open("arquivo2.txt", "w")
w.write("Esse é o meu arquivo.\n")
w.close()