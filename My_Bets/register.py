import datetime 
import json
from get import *


time = datetime.datetime.now()
today = time.date()

def register_bet():
  league = input("Nome do Campeonato: ")
  home_team = input("Time de Casa: ")
  away_team = input("Time Visitante: ")
  market = input("Mercado da Aposta: ")
  line = input("Qual linha: ")
  odd = float(input("Qual Odd da entrada: ").replace(",","."))
  value_bet = float(input("Valor da entrada: ").replace(",","."))
  result = input("1- Green | 2- Red |cd  3- Nula")
  result_money = (value_bet*odd)-value_bet if result == 1 else (value_bet if result == 3 else 0.00)

  bet = [{
    "Date" : str(today),
    "League" : league,
    "Home" : home_team,
    "Away" : away_team,
    "Market" : market,
    "Line" : line    ,
    "Odd" : odd,
    "Value" : value_bet,
    "Result" : result,
    "Money": result_money
  }]
  bet.append(get_bets()[0]) 
  with open("bets.json",'w',encoding="utf-8") as outfile:
    json.dump(bet,outfile)
    outfile.close()






