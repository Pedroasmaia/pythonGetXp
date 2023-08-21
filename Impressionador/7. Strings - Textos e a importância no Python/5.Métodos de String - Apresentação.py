#Métodos para strings
# Estrutura geralmente é : string.metodo()
##Capitalize()
print("Usando o método capitalize() para colocar 1 primeira palavra em letra maiúscula")
text = input("Insira a palavra: ")
print(text.capitalize())
#Casefold()
print("Usando o método casefold() para colocar as palavra em letra minúscula")
text = input("Insira a palavra: ")
print(text.casefold())
#Count()
print("Usando o método count() conta a quantidade dos argumentos no texto")
text = input("Insira a palavra para mostrar quantas letras (a) contem nela: ")
print(text.count('a'))
#Endswith()
print("Usando o método endswith() verifica se o texto termina com um valor espécifico ")
text = input("Coloque seu email para ver se ele termina com gmail.com: ")
#startswith()
print("Usando o método startswith() verifica se o texto começa com um valor espécifico ")
text = input("Coloque seu email para ver se ele começa com gmail.com: ")
print(text.startswith("gmail.com"))
#Find()
print("Usando o método find() para achar a posição de um texto em outro texto")
print(f"A posição do @ do seu email é no indice: {text.find('@')}")
##Isalnum()
print("Usando método isalnum() verifica se é composto por letras e numeros, sem caracteres especiais")
text = input("Coloque uma frase")
print(f"Essa frase é composta de letras e números {text.isalnum()}")
#Isalpha:
print("Usando método isalpha() verifica se ele todo composto por letras")
print(f"Essa frase é composta de letras {text.isalpha()}")
#Isnumerico
print("Usando método isnumeric() verifica se ele todo composto por números")
print(f"Essa frase é composta de letras {text.isnumeric()}")
#Replace
print("Usando o método replace(), troca um texto por outro")
texto = "pedro.maia@gmail.com"
print(texto.replace('.',','))
#split()
print("Usando o método split, separa o text de acordo com um delimitador passado como argumento")
frutas = "banana,maça,pera,tomate"
print(frutas.split(','))
#splitness()
print("Usando o método splitness, separa o text de acordo com a quebra de linha")
texto = '''
Ola, bom dia
Venho por meio desse e-email
pedir que durma bem
'''
print(texto.splitlines())
#Strip
print("O método strip() Retira cacteres indejejados,espaços por padrão")
texto = ' AABAA '
print(texto.strip())
print(texto.strip())
#Title()
print("O método title transforma a 1° letra de cada palavra maiúscula")
print(texto.title())
#Upper()
print("O método upper transforma a todas as letra de cada palavra maiúscula")
print(texto.upper())