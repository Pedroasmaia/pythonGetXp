from collections import Counter

vendas_tech = {'iphone':15000,'samsung galaxy':12000,'tv samsung':10000,'ps5':14300,'notebook hp':1000,'notebook dell':7000,'notebook asus':2450}

aux = Counter(vendas_tech)
print(aux.most_common(2))