import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Cleaning the data

pd.read_csv('flights.csv',delimiter=',',header='infer')
df = pd.DataFrame(pd.read_csv('flights.csv',delimiter=',',header='infer'))

#quiero saber cuantos datos NaN hay en cada columna
df = df.dropna()
df = df[df['ArrDelay'] < 1000]
df = df[df['DepDelay'] < 1000]


#%%

mean_Arrival = df["ArrDelay"].mean()
mean_Deppature = df["DepDelay"].mean()
print("Mean Arrival Delay: ", mean_Arrival)
print("Mean Deppature Delay: ", mean_Deppature)
#%%
plt.suptitle('Datos de llegada y salida', fontsize=16, fontweight='bold')
plt.hist(df["ArrDelay"], bins=100, range=(-50, 50), color='red', alpha=0.5, label='Llegada Delay')
plt.hist(df["DepDelay"], bins=100, range=(-50, 50), color='blue', alpha=0.5, label='Salida Delay')
plt.legend(loc='upper right')
plt.show()
#%%

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

#Creamos lso subHistogramas
ax[0].hist(df["ArrDelay"], bins=100, range=(-50, 50), color='red', alpha=0.5, label='Llegada Delay')

ax[1].hist(df["DepDelay"], bins=100, range=(-50, 50), color='blue', alpha=0.5, label='Salida Delay')
plt.subplots_adjust(wspace=0.5)
ax[0].legend(loc='upper right')
ax[1].legend(loc='upper right')
plt.suptitle('Datos de llegada y salida', fontsize=16, fontweight='bold')
plt.show()

#%%
#Ahora vamos a ver cuantas compañias aereas hay

dfCarrier = df.groupby('Carrier').mean()
dfCarrier.sort_values(by=['ArrDelay'], inplace=True, ascending=True)


plt.bar(dfCarrier.index, dfCarrier['ArrDelay'], color='red', alpha=0.7, label='Llegada Delay',)
plt.legend(loc='upper right')
plt.suptitle('Tiempos promedios de Llegada', fontsize=16, fontweight='bold')
plt.xticks(rotation=0)
plt.show()
dfCarrier.sort_values(by=['DepDelay'], inplace=True, ascending=True)
plt.bar(dfCarrier.index, dfCarrier['DepDelay'], color='blue', alpha=0.7, label='Salida Delay')
plt.legend(loc='upper right')
plt.suptitle('Tiempos promedios de Salida', fontsize=16, fontweight='bold')
plt.show()


print("Numero de compañias aereas: ", len(df['Carrier'].unique()))
print("El promedio de atrasos en la Salida es de : ", df['DepDelay'].mean())
print("El promedio de atrasos en la Llegada es de : ", df['ArrDelay'].mean())
#%%

#Ahora vamos a ver si existe alguna diferencia entre cada dia de la semana

dfDayOfWeek = df.groupby('DayOfWeek').mean()
dfDayOfWeek.head()
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
dfDayOfWeek.index = dias

plt.bar(dfDayOfWeek.index, dfDayOfWeek['ArrDelay'], color='red', alpha=0.7, label='Llegada Delay',)
plt.suptitle('Tiempos promedios de atraso de Llegada', fontsize=16, fontweight='bold')
plt.show()

print("En general el dia que mas atrasos hay en la Llegada es el", dfDayOfWeek['ArrDelay'].idxmax())

plt.bar(dfDayOfWeek.index, dfDayOfWeek['DepDelay'], color='red', alpha=0.7, label='Salida Delay',)
plt.suptitle('Tiempos promedios de atraso de Salida', fontsize=16, fontweight='bold')
plt.show()

print("En general el dia que mas atrasos hay en la Salida es el", dfDayOfWeek['ArrDelay'].idxmax(), "y es el mismo dia que mas atrasos hay en la Llegada")

#%%

#Ahora vamos a ver que aeropuertos tienen mas atrasos

aiports = df.groupby('OriginAirportID').mean()
aiports.index = aiports.index.astype(str)
airports = aiports.sort_values(by=['ArrDelay'], ascending=True)

plt.bar(aiports.index, aiports['ArrDelay'], color='red', alpha=0.7, label='Llegada Delay',width=0.5,)
plt.suptitle('Tiempos promedios de atraso de Llegada de los Aerepuertos', fontsize=16, fontweight='bold')
plt.show()
#%%

#Ahora vamos a ver que la ruta tienen mas atrasos
#%%

#Veremos que ruta tiene mas atrasos en promedio

routes = df.groupby(['OriginAirportID', 'DestAirportID']).mean()
routes.index = routes.index.to_series().apply(lambda x: str(x[0]) + ' - ' + str(x[1]))
routes = routes.sort_values(by=['ArrDelay'], ascending=True)
print("La ruta con mas atrasos es: ", routes['ArrDelay'].idxmax())




