'''
Alex acabou de ganhar um novo bambolê, ele adora, mas se sente desanimado porque seu irmãozinho é melhor do que ele.

Alex consegue 10 ou mais argolas, retorna a string "Ótimo, agora passe para as manobras". 
Se ele não conseguir 10 aros, devolva a string "Continue até conseguir".

'''
def hoop_count(n):
    if n >= 10:
        return("Great, now move on to tricks")
    else:
        return("Keep at it until you get it")
print(hoop_count(10))