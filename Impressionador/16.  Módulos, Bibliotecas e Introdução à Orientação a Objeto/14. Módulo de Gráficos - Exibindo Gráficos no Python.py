import matplotlib as plt
vendas = [1500,1727,1350,999,1050,1027,1022,1500,2000,2362,2100,2762]
meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dev']

plt.plot(meses,vendas)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0,12,0,max(vendas)+500])
plt.show()