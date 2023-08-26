#Cada item na lista é uma lista
vendedores = ['Lira','João','Diego','Alan']
produtos = ['ipad','iphone']
vendas = [
    [100,200],
    [300,500],
    [50,1000],
    [900,10],
]
print(f'{vendedores[1]} vendeu {vendas[1][0]} Ipads')
print(f'{vendedores[2]} vendeu {vendas[2][1]} Iphone')
vendas_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print(f'Vendeu um total de R${vendas_iphone:.2f}')


#Modificar na lista
vendas[0][1] = 50
print(vendas)

#Adicionar um item na lista dentro da lista
produtos.append('mac')
vendas_mac = [10,15,6,70]
vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])
print(produtos)
print(vendas)
