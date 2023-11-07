import time
import locale
# Usando os nomes do BRzão:
locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
print(type(tempo_em_struct))

print('time.strftime() converte o time.struct_time no formato que eu desejar:')
'''
%d Dia do mês
%B Mês
%Y Ano
'''

print(time.strftime('%d %B %Y',tempo_em_struct))

'''
%H Hora
%M Minutos
%S Segundos

'''
print(time.strftime("%H:%M:%S",tempo_em_struct))

'''
%A Dia da Semana não abreviado
%d Dia do mês
%B Mês
%Y Ano
%H Hora
%M Minutos
%S Segundos

'''
print(f'Executado numa {time.strftime("%A de %B de %Y, %H:%M:%S")} ')

print('Fazer uma string virar um struct_time com strptime()')
string_tempo = '30 Junho,2023'
formato = '%d %B,%Y'
print(f'o Tempo é: {string_tempo}')
print(time.strptime(string_tempo,formato)) 

date = input('Insira uma data com esse formato dia/mês/ano:')
formato = "%d/%m/%Y"
print(time.strptime(date,formato))

print('gmtime() transforma struct_time em UTC')
time.gmtime(0) #Time epoch, por padrão pega o time atual

print(f'Tempo atual em UTC: {time.gmtime}')


print('time.mktime() converte um struct_time para segundos desde a epoch')

tempo_em_struct = time.localtime()
tempo_em_segundos = time.mktime(tempo_em_struct)
print(f'Tempo em segundos {tempo_em_segundos}')
print(f'Tempo em segundos {time.time()}')