import time
import locale

locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')
'''
Crie um script que moste quandos dias horas minutos faltam até o proximo ano Novo
'''
actual_time = time.localtime()
new_year = (actual_time.tm_year +1,1,1,0,0,0,0,0,0)
new_year_epoch = time.mktime(new_year)
actual_time_epoch = time.mktime(actual_time)
missing_time_epoch = new_year_epoch - actual_time_epoch

seconds_per_minutes = 60
seconds_per_hour = 60 * 60
seconds_per_day = 24 * 60 * 60

days,restos_segundos = divmod(missing_time_epoch,seconds_per_day)
hours, restos_segundos = divmod(restos_segundos,seconds_per_hour)
minutes, restos_segundos = divmod(restos_segundos,seconds_per_minutes)

print(f'Está faltando {days} dias, {hours} horas. {minutes} minutos e {restos_segundos} segundos')