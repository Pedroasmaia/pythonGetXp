from datetime import datetime,date,timedelta

print('-----------------')
print("Datetime")
print('-----------------')
agora = datetime.now()
print(f'Data: {agora.date()}')
print(f'Horário: {agora.time()}')
print(f'Ano: {agora.year}')
print(f'Mês: {agora.month}')
print(f'Dia: {agora.day}')
print(f'Hora: {agora.hour}')
print(f'Minuto: {agora.minute}')
print(f'Segundos: {agora.second}')

print('-----------------')
print("Date")
print('-----------------')
hoje = date.today()
print(f'Ano: {hoje.year}')
print(f'Mês: {hoje.month}')
print(f'Dia: {hoje.day}')

print('-----------------')
print("Timedelta")
print('-----------------')

data_atual = datetime.now()
print(f'Data Atual: {data_atual}')  
data_futura = data_atual +timedelta(days=10)
print(f'Data 10 dias no futuro {data_futura}')
data_passada = data_atual - timedelta(days=10)
print(f'Data 10 dias no passado {data_passada}')
hora_futura = data_atual + timedelta(hours=10)
print(f'Hora futura: {hora_futura}')

meu_aniversario = datetime(2000,1,8)
print(meu_aniversario)
data_iso = datetime.fromisoformat('2000-01-08 10:35:59')
print(f'Data/hora: {data_iso}')

data1 = datetime(2023,6,25)
data2 = datetime(1995,1,30)
diferenca = data1 - data2
print(f'A Diferença é {diferenca.days} dias')
if data1 > data2:
    print(f'A Data posterior data é {data1}')
else:
    print(f'A Data anterior é {data2}')

datas = [
    datetime(2020,6,6),
    datetime(2021,9,4),
    datetime(2021,7,30),
    datetime(2019,1,2)
]
datas = sorted(datas)

print(datas)

for data in datas:
    print(data)