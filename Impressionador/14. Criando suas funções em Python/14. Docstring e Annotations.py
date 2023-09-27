print("Docstring é a explicação do que a função faz")

def minha_função():
    ''' Essa é a descrição da minha função
    
    Parameters:
        num1 (int): A Explicação do parametro
    
    Returns:
        num1(int): Aquilo que a funcion retorna
    '''

print('Annotation')

def minha_soma(num1:int,num2:int,num3:int)-> int:
    return num1+num2+num3