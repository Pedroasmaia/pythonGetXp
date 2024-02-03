'''
Crie um script python que mostra quanto tempo se passou desde a última compra do cliente(10 de Maio de 2023), SE FAZ MAIS DE 30 DIAS mostre uma mensagem oferecendo desconto
'''
from datetime import *
import locale

locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')
ultima_compra = datetime(2023,5,10)
agora = datetime.now()
intervalo_compras =  agora - timedelta(days=ultima_compra.day)
print(intervalo_compras.day)


