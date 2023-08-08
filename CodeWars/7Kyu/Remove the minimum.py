# Dada uma matriz de inteiros, remova o menor valor. Não altere a matriz/lista original. Se houver vários elementos com o mesmo valor, remova aquele com um índice menor. Se você obtiver um array/lista vazio, retorne um array/lista vazio.

# Não altere a ordem dos elementos restantes.

def remove_smallest(numbers):
    if not numbers:  # Verifica se a lista está vazia
        return []

    numbers_copy = numbers.copy()  # Cria uma cópia da lista original
    min_value = min(numbers_copy)    # Encontra o menor valor

    numbers_copy.remove(min_value)   # Remove o menor valor da cópia

    return numbers_copy
