import math
import random

base_xp = lambda level: (4*math.pow(level,3))/5
levels_por_xp = lambda xp: int(((5 * xp) / 4) ** (1/3))
gain_xp = lambda oponente_level: (oponente_level*base_xp(oponente_level))/2 
def battle():
  inimigo_level = 1
  exp_won = gain_xp(inimigo_level)
  print(f'O Inimigo é do level {inimigo_level} ')
  print(f'Você ganhou {exp_won:.2f} pontos')
  return exp_won

def nivel(level):
  return base_xp(level) 

def next_nivel(level):
  return base_xp(level+1) - base_xp(level)

level = 1
exp_points = 0
exp_points = nivel(level)
exp_to_promo = next_nivel(level)

print(f'Nivel Atual: {level}')
print(f'Pontos de EXP: {exp_points:.2f}')
print(f'Pontos para proximo nivel {exp_to_promo:.2f}')

exp_points += battle()
level = levels_por_xp(exp_points)
print('------------------------------------------')
print(f'Nivel Atual: {level}')
print(f'Pontos de EXP: {exp_points:.2f}')
print(f'Pontos para proximo nivel {exp_to_promo:.2f}')
print('------------------------------------------')
