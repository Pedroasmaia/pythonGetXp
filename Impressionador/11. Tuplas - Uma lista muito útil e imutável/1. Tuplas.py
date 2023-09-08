tulpa = ('valor','valor','valor')
#São imutaveis
#Mais eficiente em performance
#Protege os dados
#São muito usados para dados heterogêneos

pessoa = ('Pedro','25/08/2020','08/01/2000',1000,'Estagiário')

try:
    pessoa[3] = 3000
except TypeError:
    print('Tuplas não podem ser modificadas')
nome = pessoa[0]
data_contratação = pessoa[1]
data_nascimento = pessoa[2]
salario = pessoa[3]
cargo = pessoa[4]

print(nome,data_contratação,data_nascimento,salario,cargo)
