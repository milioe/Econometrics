

#Autor: Humberto Acevedo Cruz
#Fecha de creación:05/08/2021
#Última modificación:05/08/2021 17:24 hrs
#Objetivo del módulo o programa:
#Obtener el mejor ajuste lineal de los siguientes conjuntos de datos.
#------------------------------------------------------------------

#Librerias

import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []
with open("Salary_Data.csv") as insumo:
    reader = csv.reader(insumo, delimiter=",")
    next (reader)
    for row in reader:
        a = float(row[0]) 
        x.append(a)
        b = float(row[1]) 
        y.append(b)


# x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# y =[1,2,2,4,5,4,6,4,6,7,9,10,11,12,10]

x=np.array(x)
y=np.array(y)

n=len(x)
sumx=sum(x)
sumy=sum(y)
sumy2=sum(y*y)
sumx2=sum(x*x)
sumxy=sum(x*y)
promx=sumx/n
promy=sumy/n

m=(sumx*sumy- n*sumxy) / (sumx**2 - n *sumx2)

b = promy - m*promx

#Gráfica 

plt.scatter(x,y, color="red")
plt.plot(x, m*x+b, label="Ajuste")

plt.xlabel("Años de experiencia")
plt.ylabel("Saalario")
plt.title("Regresión Lineal Simple")
plt.grid()
plt.legend
plt.show

sigmax = np.sqrt(sumx2/n - promx**2)
sigmay = np.sqrt(sumy2/n - promy**2)
sigmaxy = sumxy/n - promx*promy
R2 = (sigmaxy/(sigmax*sigmay))**2


#Para alguien que tiene 1 años de experiencia 
# ¿Cuanto se espera que gane?

pronostico= b + (m*1)
print(pronostico)

