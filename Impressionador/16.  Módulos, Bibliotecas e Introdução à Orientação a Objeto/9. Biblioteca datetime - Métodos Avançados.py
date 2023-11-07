from datetime import datetime, timezone,timedelta
import locale
from zoneinfo import ZoneInfo

locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')

agora = datetime.now()

print(type(agora))

print(agora.strftime("%A, %d de %B de %Y, %H:%M:%S"))
string_data = "09/06/2023, 15:30:20"
formato = "%d/%m/%Y, %H:%M:%S"
data = datetime.strptime(string_data,formato)
print(type(data))
data_hora = datetime(2023,6,26,15,30,20)
print(f'Data/hora: {data_hora}')

fuso_horaio = timezone.utc
data_hora = datetime(2023,6,26,15,30,20,tzinfo=fuso_horaio)
print(data_hora)
fuso_horaio_sp = timezone(timedelta(hours=-3))
data_hora = datetime(2023,6,26,15,30,20,tzinfo=fuso_horaio_sp)
print(data_hora)
fuso_horaio_los_angeles = ZoneInfo('America/Los_Angeles')
data_hora = datetime(2023,6,26,15,30,20,tzinfo=fuso_horaio_los_angeles)
print(f"Data em Los Angeles {data_hora}")

print('Converter fuso horário')
fuso_horaio_sp = ZoneInfo('America/Sao_Paulo')
data_hora = datetime(2023,6,26,15,30,20,tzinfo=fuso_horaio_sp)
fuso_horaio_ny = ZoneInfo('America/New_York')
data_hora_ny = data_hora.astimezone(fuso_horaio_ny)
print(f"{data_hora} em sp")
print(f"{data_hora_ny} em ny")