lista = [150,10,30,2000,90]
lista.sort()
print(lista)

#Criando function

def cadastrar_produto():
    produto = input('Digite o nome do produto: ')
    print(f'Produto: {produto.title()} cadastrado com sucesso')

for i in range(3):
    cadastrar_produto()