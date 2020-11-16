""" -*- coding: utf-8 -*-
Ordenação de Listas """

lista = [124, 345, 72, 46, 6, 7, 3, 1, 7, 0]

""" ele retorna a lista original, nao altera nenhum valor"""
lista.sort()

print(lista)

""" requer que retorne um valor"""

lista2 = [23, 3, 4]

lista2 = sorted(lista2)

print(lista2)

""" ordenação decrescente """

lista.sort(reverse=True)

print(lista)

""" inverter lista """

lista.reverse()
print(lista)

""" listas de strings ordenadas alfabeticamente """
lista3 = ["bola", "abacate", "dinheiro"]

lista3.sort()
print(lista3)

lista3.sort(reverse=True)

print(lista3)

""" Dicionário -> arrays associativos por valor(es) vinculados 
a uma chave para o valor correspondente"""

dicionario_sites = {"Amanda": "Amanda Israel"}

print(dicionario_sites['Amanda'])

meu_dicionario = {"A":"AMEIXA", "B": "BOLA", "C": "CACHORRO"}

print(meu_dicionario)
print(meu_dicionario["A"])

for chave in meu_dicionario:
	print(chave+":"+ meu_dicionario[chave])

""" retorna todos os itens/ valores/ chaves. Converte o dicionario para uma tupla -
	conjunto de dados imutaveis (tipos heterogêneos)
"""
for chave in meu_dicionario.items():
	print(chave)

for chave in meu_dicionario.values():
	print(chave)

for chave in meu_dicionario.keys():
	print(chave)
