import datetime 
import json
from get import *
from register import *
def menu():
   tam = 30
   options = {
      "1" : "Registrar Bet",
      "2" : "Mostrar Bets",
      "0" : "Sair"
   }
   while True:
      print(f"+{'-'*tam}+")
      print(f"|{'Menu':^{tam}}")
      print(f"+{'-'*tam}+")
      for k,v in options.items():
        print(f"|{f'{k} - {v}':{tam}}|")
      print(f"+{'-'*tam}+")
      op = input()
      
      
      if op not in options:
         print("Opção invalída")
         continue
      if op == "0":
         break 
      if op == "1":
         register_bet()
      if op == "2":
         print(get_bets())
menu()