""" -*- coding: utf-8 -*- """
""" 
1. Enumerate
2. List comprehension
3. Map
4. Reduce
5. Zip
6. Filter
""" 
""" enumerate = enumerar elementos dentro de uma lista junto com o nome do elemento
Forma não Pythoniana:

lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
	print(i, lista[i])

	--> vai pegar o tamanho da lista e armazenar em um vetor (range) 
	e assim imprimir a posição e mostrar o conteúdo naquela posição
"""
lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate(lista):
	print(i, nome)

""" List comprehension 

x = [1, 2, 3, 4, 5]
y = []

for i in x:
	y.append(i**2)

print(x, y)
"""
x = [1, 2, 3, 4, 5]
"""y = [valor_a_adicionar laço condição]"""
y = [i ** 2 for i in x]
z = [i for i in x if i%2 == 1]
print(x, y, z)

""" Map = pegar uma função e aplicar a todos os elementos de uma lista 
Ex: quando enviado um vetor a uma função que duplica aquilo que é mandado, 
a função acaba duplicando o vetor, em vez dos valores dentro dele e isso pode 
ser um problema, por isso a utilização da função Map
"""

def dobro(x):
	return x*2

valor = 2
valor1 = [1,2,3,4,5]
print(dobro(valor))
print(dobro(valor1))

for valor_dobrado in (map(dobro, valor1)):
	print(valor_dobrado)

valor_dobrado = list(map(dobro, valor1))
print(valor_dobrado)

""" Reduce = recebe uma lista e retorna um único valor a ela"""

from functools import reduce

def soma(x, y):
	return x+y

lista = [1, 3, 5, 10, 20]

soma = reduce(soma, lista)
print(soma)

""" Zip = compactar duas listas como se fosse uma só em um laço for """

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$ 2,00", "R$ 5,00", "N", "N", "N"]

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)

""" Filter  = função usada para filtrar elementos de uma lista"""

def dobro(i):
	if i%2 == 0:
		return i

lista = [1, 2, 3]
lista2 = filter(dobro, lista)
lista2 = list(lista2)
print(lista2)