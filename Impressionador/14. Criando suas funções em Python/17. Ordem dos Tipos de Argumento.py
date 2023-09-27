print('Primeiro os posicionais e depois os de keyword')
print('Primeiro os argumentos individuais depois os multiplos')
def minha_soma(*numeros,num1):
    soma = 0
    for numero in numeros:
        soma += numero
    soma += num1
    return soma
# Repare que o num1 virou keyword
print(minha_soma(2,5,1,num1=5))
