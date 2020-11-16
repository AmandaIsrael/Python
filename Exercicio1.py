""" -*- coding: utf-8 -*-

 Maior ou menor de idade """


usuario = 12
usuario2 = 23

if usuario2 < 18:
 	print("Menor de idade")
else:
 	print("Maior de idade")

nota1 = 7.0
nota2 = 5.0

if nota2 > 6:
	print("Aprovado")
else:
	print("Reprovado")

a = 2
b = -3
c = -5

delta = (b**2 - 4*a*c)**0.5
print(delta)

x1 = -b + delta
x1 /= 2*a

x2 = -b - delta
x2 /= 2*a

print("x1 =", x1)
print("x2 =", x2)

lista = [12,2,0]
lista.sort();
print(lista)

x = 10;
y = 3
sinal = "+";

menos = sinal.find("-")
mais = sinal.find("+")
vezes = sinal.find("*")
divisao = sinal.find("/")

if menos != -1:
	print(x, sinal, y, "=", x-y)
else:
	if mais != -1:
		print(x, sinal, y, "=", x+y)
	else:
		if vezes != -1:
			print(x, sinal, y, "=", x*y)
		else:
			if divisao != -1:
				print(x, sinal, y, "=", x/y)


print("----------------------------------------")
""" Respostas: 

import: """

idade = int(input("Digite sua idade: "))

if idade >= 18:
	print("Maior de idade")
elif idade < 18:
	print("Menor de idade")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

if media >= 6:
	print("Aprovado")
else:
	print("Reprovado")


""" importar biblioteca """

from math import sqrt

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)
 
if raiz_delta < 0:
    print("Delta negativo")
else:
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b + raiz_delta)/2*a
 
    print("As raízes são", x1, "e", x2)


lista = [3,2,1]
print(sorted(lista))


n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))
 
if sinal == "+":
    op = n1 + n2
 
elif sinal == "-":
    op = n1 - n2
 
elif sinal == "/":
    op = n1 + n2
 
elif sinal == "*":
    op = n1 * n2
 
else:
    print("Sinal inválido.")
 
print(op)