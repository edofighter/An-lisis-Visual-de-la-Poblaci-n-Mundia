import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#leer y ajustar indice
dfpob = pd.read_csv('poblacion/API_SP.POP.TOTL_DS2_es_csv_v2_21827.csv',skiprows=3)
dfpob.set_index('Country Code', inplace=True)
print(dfpob.head())

#Lista de columnas de años (como strings)
dfpob2 =[str(k) for k in range (1960,2024)] 

#Lista de códigos de países
paises = ['CHL','AGO','MEX','ESP']

#Filtramos DataFrame: filas (paises), columnas (años)
dfpob3 = dfpob.loc[paises,dfpob2]
print(dfpob3)

#graficos 1 Evolución de la población (líneas)
plt.figure(figsize = (12,6))
for pais in paises:  plt.plot(dfpob3.loc[pais],label = pais)
plt.legend()
plt.grid()
xvalues = np.arange(1960, 2024, 5)
xvalues = [str(k) for k in xvalues]
plt.xticks(xvalues)
plt.title('Evolución de la población')
plt.show()

#graficos 2 Comparación de población 1960 vs 2023 (barras)
plt.figure(figsize=(12,6))
ancho_barras = 0.35
plt.grid()
indice_barras = np.arange(4)
plt.bar(indice_barras,dfpob3['1960'], width= ancho_barras, label = '1960')
plt.bar(indice_barras + ancho_barras,dfpob3['2023'], width= ancho_barras, label = '2023')
plt.xticks(indice_barras + ancho_barras, dfpob3.index)
plt.title('Comparación de población 1960 vs 2023')
plt.legend()
plt.show()

#graficos 3 1960 Pie chart población 1960
plt.figure(figsize=(12,6))
plt.title('Distribución de Población - 1960')
plt.pie(dfpob3['1960'], labels=dfpob3.index, shadow=True, autopct='%1.2f%%')
plt.show()

#graficos 4 2023 Pie chart población 2023
plt.figure(figsize=(12,6))
plt.title('Distribución de Población - 2023')
plt.pie(dfpob3['2023'], labels=dfpob3.index, shadow=True, autopct='%1.2f%%')
plt.show()