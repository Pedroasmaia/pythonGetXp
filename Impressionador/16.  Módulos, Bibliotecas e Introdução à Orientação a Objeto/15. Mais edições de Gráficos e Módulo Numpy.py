import matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(1000,3000,50)
meses = np.arange(1,51)
def dispersão():
    plt.axis([0,50,0,max(vendas)+200],color='red')
    plt.plot(meses,vendas)
    plt.xlabel('Meses')
    plt.ylabel('Vendas')
    plt.show()

def dispersão():
    plt.scatter(meses,vendas)
    plt.show()
def barras():
    plt.bar(meses,vendas)
    plt.show()

plt.figure(1,figsize=(17,3))
#Linhas Colunas Atual
plt.subplot(1,3,1)
plt.axis([0,50,0,max(vendas)+200],color='red')
plt.plot(meses,vendas)
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.subplot(1,3,2)
plt.scatter(meses,vendas)
plt.subplot(1,3,3)
plt.bar(meses,vendas)
