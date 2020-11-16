"""
Os operadores lógicos são categorizados como: AND, OR e NOT

"""
x = 3; y = 3; z = 4
print(x == y or x == z and z == y)

"""
Sintaxe condição if <.>

if condição:
	execute_esta_linha
else:
	caso_if_falhe_execute_esta_linha

"""
# -*- coding: uft-8 -*-
x = 1
y = 2

if x > y:
	print("x é maior que y")
else:
	print("y é maior que x")

#o comando elif é pra representar 'else if' em uma condição

if x == y:
	print("Números iguais.")
else: 
	if x < y:
		print("x é menor que y")
	else:
		print("x é maior que y")
		
