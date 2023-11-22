vendas_produtos = [1500,150,2100,1950]
produtos = ['vinho','cafeiteira','microondas','iphone']

lista_aux = list(zip(vendas_produtos,produtos))
lista_aux.sort(reverse=True)
print(lista_aux)
#List Comprehension com unpacking de Tupla
mais_vendidos = [produto for vendas,produto in lista_aux]
print(mais_vendidos)