# Função upper() não tem parâmetro nenhum
cod = 'beb12304'
print(cod.upper())
# Função sort() precisa de um parametro de posição
venda = [10,20,64,984,6412,65]
print(venda.sort(reverse=True))

#Extend só recebe um parametro de posição
vendanove = [10,20,6080]
venda.extend(vendanove)

# Nossa função tem 2 parÂmetros de posição obrigatórios
def eh_da_categoria(bebida,cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False
