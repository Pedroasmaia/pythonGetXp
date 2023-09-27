produtos = ['apple tv','mac','iphone x','iPad','apple watch','mac book','airpods']

produtos.sort()
print('Sem passar o parametro padrão: ')
print(produtos)
print('Passando o parametro padrão: ')
produtos.sort(reverse=True)
print(produtos)


def padronizar_codigos(lista_codigos,padrao='m'):
    for i,item in enumerate(lista_codigos):
        item = item.replace('  ',' ')
        item = item.strip()
        if padrao == 'm':
            lista_codigos[i] = item.casefold()
        elif padrao == 'M':
            lista_codigos[i] = item.upper()

        else:
            print('Insira M para maiusculas e m para minusculas')
    return lista_codigos

cod_produtos = ['  ABC12 ','abc34','AbC37']
print('Sem passar o parametro padrão: ')
print(padronizar_codigos(cod_produtos))
print('Passando o parametro padrão: ')
print(padronizar_codigos(cod_produtos,'M'))