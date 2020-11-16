#laços de repetição

"""
i = 0
while i < 5:
	print (i)
	i = i + 1
"""
x = 1
while x < 10:
	print(x)
	x = x + 1 # or could be x += 1 but not ++x or x++

print("--------------------------------------------")

"""
for
lista é tipo os vetores de Python
"""
lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0, "ola","biscoito","bolacha",9.99,True]

for i in lista3:
	print(i)

"""
função range vai me dar um parametro de onde começar uma contagem

for i in rangue(10):
	print(i) -> retorna lista que contém 10 elementos

for i in rangue(10, 20): ->contagem de 10 até 20
	print(i)
"""