"Um usuário fornece sua data de nascimento no formato dd/mm/aaa.Crie um script para calcular a idade do usuario:"

from datetime import *

now = datetime.now()
birthday_date = input('Insira uma data no formato dia/mês/ano: ')
birthday_date = datetime.strptime(birthday_date,"%d/%m/%Y")
actual_month = now.month
actual_day = now.day

birthday_month = birthday_date.month
birthday_day = birthday_date.day

if birthday_month > actual_month:
        print(f'Você tem {(now.year - birthday_date.year) - 1} anos')
elif birthday_month == actual_month and birthday_day > actual_day :
        print(f'Você tem {(now.year - birthday_date.year) - 1} anos')
else:
        print(f'Você tem {now.year - birthday_date.year} anos')



