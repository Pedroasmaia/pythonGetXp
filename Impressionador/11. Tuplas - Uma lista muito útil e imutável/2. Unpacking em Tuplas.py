vendas = ('Pedro','25/08/2020','08/01/2000',1000,'Estagiário')

nome,data_contratação,data_nascimento,salario,cargo = vendas
print(nome)
print(data_contratação)
print(data_nascimento)
print(salario)
print(cargo)

vendas = [1000,2000,300,300,150]
funcionarios = ['Joao','Lira','Ana','Maria','Paula']

for item in enumerate(vendas):
    i,venda = item
    print(f'{funcionarios[i]},vendeu {venda} unidades')