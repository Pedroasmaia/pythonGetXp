import time
import locale

locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')
'''
Contagem regressiva:
Um Evento especial está programado para começar em 10 segundos. Crie uma contagem regressiva que começa em 10 e vai até 0, com uma pausa de um segundo entre cada número.
'''
for sec in range(10,0,-1):
    print(sec,end=" \r")
    time.sleep(1)

print('Começou!!!')


'''
Uma empresa quer exibir a data e a hora atual em seu site no formato:
(Dia da Semana), (dia do mês) de (mês do ano), (horas):(minutos)
'''
time_actual = time.localtime()
print(time.strftime('%A,%d de %B %Y, %H:%M'))