from flask import Flask
import pandas as pd
tabela = pd.read_excel(r"Impressionador\33. Integração Python com APIs e JSON\Vendas - Dez.xlsx")
app = Flask(__name__)


@app.route("/")
def calc_faturamento():
  faturamento = tabela["Valor Final"].sum()
  return  {"Faturamento":float(faturamento)}
@app.route("/vendas/produtos") #Decorator -> diz em qul link a func vai rodar
def vendas_produtos(): #Define função
  tabela_venda_produtos = tabela[["Produto","Valor Final"]].groupby("Produto").sum()
  dict_venda_produtos = tabela_venda_produtos.to_dict()
  return dict_venda_produtos
@app.route(f"/vendas/<produto>") #Decorator -> diz em qul link a func vai rodar
def faturamento_produto(produto):
  tabela_venda_produtos = tabela[["Produto","Valor Final"]].groupby("Produto").sum()
  if produto in tabela_venda_produtos.index:
    vendas_produto = tabela_venda_produtos.loc[produto]
    dict_venda_produtos = vendas_produto.to_dict()
    return {produto : dict_venda_produtos}
  else:
    return {produto : "Inexistente"}
app.run(debug=True)