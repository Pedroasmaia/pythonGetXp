faturamento = 2000
custo = 500
lucro = faturamento - custo
print('Usando o str() e concatenando com + : ')
print('O faturamento da loja foi de: ' + str(faturamento) + ' o Custo foi de' + str(custo) + 'O  Lucro foi de ' + str(lucro))
print('Usando o Format')
print('O Faturamento foi de {0}, o custo foi de {1} e o lucro foi de {2}. Lembrando o Faturamento foi {0}'.format(faturamento,custo,lucro))
print('Usando Fstrings')
print(f'O Faturamento foi de {faturamento} o custo foi de {custo} e o lucro foi de {lucro}')
print("Usando o %s, usado para string e %d , usada para número")
print('O faturamento foi de : %d. O Custo foi de %d e o lucro foi de %d' % (faturamento,custo,lucro))
print('Uso do IN:')
print('@' in 'lira@gmail.com')
print('@' in 'lira.gmail.com')