# String
# concatenação de string

a = "Ola "
b = "mundo"

concatenar = a + b
print(concatenar)

# tamanho de string

tamanho = len(concatenar)
print(tamanho)

# navegar pela string

for i in concatenar:
	print(i)
print(" ")

x = 0
while x < 9:
	print(concatenar[x])
	x += 1

# Imprimir parte de uma string

print(concatenar[0:3])

# em Python, string (e a maioria das coisas) são objetos
# Entao pode-se aplicar métodos as strings

# Função para remover espaço ou caracter especial da string

pessoa = "Pessoa" + "\n"
print(pessoa.strip())

# Deixar as palavras em minusculo

palavra = "AMANDA"
palavra = palavra[0] + palavra[1:6].lower()
print(palavra.strip())

# Deixar as palavras maiusculas

print(concatenar.upper())

# converção de sequencias em listas

string = "O rato roeu a roupa do rei de Roma"
lista = string.split(" ")
print(lista)

# quebrar string por letras
# Case sensitive é atribuido a essa função

lista = string.split("r")
print(lista)

# Busca de substring -> função retorna a posição do primeiro caractere da palavra procurada
# Se a substring nao for encontrada é retornado -1

busca = string.find("rei")
print(string[busca: 26])

# substituir parte de uma string

string = string.replace("o rei", "a rainha")
print(string)
