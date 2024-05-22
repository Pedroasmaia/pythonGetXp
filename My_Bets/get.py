import json

def get_bets():
  with open("bets.json", "r", encoding="utf-8") as infile:
      all_bets = json.load(infile)
      infile.close()
  return all_bets