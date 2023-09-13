produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'notebook hp', 'notebook dell', 'notebook asus']
valores = [15000, 12000, 10000, 14300, 1000, 17000, 2450]
print('dict.fromkeys() cria um dicionario com valores padrão. Exemplo:')
new_dict = dict.fromkeys(produtos,0)
print(new_dict)

print('dict() transforma lista de tuplas')
vendas = [
('20/08/2020','iphone x'),
('21/08/2020','ipad'),
]

dict_vendas = dict(vendas)
print(dict_vendas)


print('Transformar duas listas em um dicionario, Primeiro transforme ela em tuplas com o método zip()')

lista_tuplas = zip(produtos,valores)
dicionario_lista = dict(lista_tuplas)
print(dicionario_lista)