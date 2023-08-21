print('Posso pegar indices de tras pra frente usando o negativo:')
print(
'''
-5 -4 -3 -2 -1
 P  e  d  r  o
'''
)
nome = input('Coloque seu nome: ')
print(f"Pegando a ultima letra do seu nome: {nome[-1]}")

print('Posso pegar pedaço do texto usando inicio:fim')
print('''
      
Quero desconsiderar a primeira letra e a ultima de uma palavra
      palavara[1:-1]
      ''')
palavra = input('Digite uma palavra: ')
print(palavra[1:-1])


# Exercicio de Fixação

print('Tamanho da palavra: ' + str(len(palavra)) + ' caractetes')
print('Primeiro Caractere ' + palavra[0])
print('Ultimo Caractere ' + palavra[-1])