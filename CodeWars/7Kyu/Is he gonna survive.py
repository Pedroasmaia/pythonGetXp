'''
Um herói está a caminho do castelo para completar sua missão.
No entanto, ele foi informado de que o castelo está cercado por alguns dragões poderosos! cada dragão leva 2 balas para ser derrotado, nosso herói não tem ideia de quantas balas ele deve carregar. Supondo que ele pegue um número específico de balas e avance para lutar contra outro número específico de dragões, ele sobreviverá? Retorne verdadeiro se sim, falso caso contrário :)
'''
def hero(bullets, dragons):
    return dragons % (bullets * 2) == 0
hero(32,10)