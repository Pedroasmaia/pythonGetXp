vendas = [941,852,783,714,697,686,685,670,631,453,47]
vendedores = ['Maria','Jose','Antonio','Joao','Fransisco','Ana','Luiz', 'Paulo','Carlos','Manoel','Pedro']
meta = 50


i = 0
try:
    while vendas[i] > meta:
        print(f'{vendedores[i]} bateu a meta. Vendas {vendas[i]}')
        i+=1
except IndexError:
        print('Finalizamos o Array')
        