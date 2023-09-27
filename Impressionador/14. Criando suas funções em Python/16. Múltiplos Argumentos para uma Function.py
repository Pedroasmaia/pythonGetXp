'''
*args -> Para argumentos posicionais

**kwargs -> Para Agumentos em formato de keywords
'''

def minha_soma(*numeros):
    print(f'O argumento vem como uma tupla: {numeros}')
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
print(minha_soma(10,13,1,90,0,9,0))

def preco_final(preco,**adicionais):
    print(f'O argumento vem como dicionario {adicionais}')
    if 'desconto' in adicionais:
        preco *= (1-adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco
print(preco_final(1000,desconto=0.1,garantia_extra=100))
