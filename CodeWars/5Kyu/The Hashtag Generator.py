def generate_hashtag(s):
    s = s.title()
    ponto = str.maketrans("","","  ")
    s = s.translate(ponto)
    s = s.strip()
    if len(s) > 139:
        return False
    elif len(s) == 0:
        return False
    return "#"+s
print(generate_hashtag("    hello     world   "))
    #maketrans(tenho,quero_colocar,quero_remover)
#translate(aplica a mascara criada pelo maketrans)