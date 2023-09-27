print('O Return sempre finaliza a Function:')
def minha_soma(a,b,c):
    return a + b + c
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  "," ")
    texto = texto.strip()
    return texto
def bate_meta(vendas,meta):
    if vendas >= meta:
        return True
    else:
        return False
def filtrar_lista_texto(lista,pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
            return lista_filtrada

lista_texto = ['a@gmail.com','a@outlook.com','b@gmail.com','c@gmail.com']
lista = filtrar_lista_texto(lista_texto,'outlook')
print(lista)

