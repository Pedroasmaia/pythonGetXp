#Escreva uma função que retorne uma string na qual o nome é trocado pelo sobrenome.
def name_shuffler(str_):
    first_name,second_name = str_.split(' ')
    return second_name+" "+first_name