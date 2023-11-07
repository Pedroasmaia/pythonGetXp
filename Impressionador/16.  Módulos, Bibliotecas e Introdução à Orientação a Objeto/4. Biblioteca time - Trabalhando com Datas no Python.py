import time

tempo_Atual = time.time()
print(tempo_Atual)
tempo_anual_nanosegundos = time.time_ns()
print(tempo_anual_nanosegundos)

inicio = time.time()

for i  in range(600_000_00):
    pass

fim = time.time()

print(f'Rodou em {fim - inicio} segundos')


print(f'Espere 5 segundos')
time.sleep(5)
print('Passou 5 segundos')

tempo_em_segudos = time.time()
tempo_local = time.ctime(tempo_em_segudos)
print('ctime() converte o tempo em segundos no tempo atual')
print(f'Tempo local: {tempo_local}')

tempo_em_segudos = time.time()
tempo_local = time.localtime(tempo_em_segudos)
print(f'locatltime retorna essa tupla {tempo_local}')
print('Que posso isolar:')
print(f'Ano: {tempo_local.tm_year}')
print(f'Mês:{tempo_local.tm_mon}')
print(f'Mês:{tempo_local.tm_mday}')

print(f'time.time() pega a data em seg desde epoch | {time.time()}')
print(f'time.ctime(time.time) retorna uma string revelando informações com a hora atual | {time.ctime(time.time())}')
print(f'time.localtime() retorna uma tupla, com atributos da hora | {time.localtime()}')