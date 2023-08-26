# Alterações "Incrementais"

lista = ['mac','iphone']
vendas = [100,200]

#Adicionar Ipad na lista
lista += ['ipad']

#Adicionar 500 vendas
soma_vendas = 300
soma_vendas += 500

email = 'Esse mês vendemos um total de {} produtos, sendo \n {} unidades de {}'.format(soma_vendas,vendas[0],lista[0])
email = email + '\n {} unidades de Ipad'.format(700)
print(email)