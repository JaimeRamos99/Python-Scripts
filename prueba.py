# -*- coding: utf-8 -*-
"""prueba.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L_6ptnrteOfVmNg-NM0RO6G9JcprAZgQ

trabajando con tensores
"""

import torch
import numpy as np
import pandas as pd
tensorA= torch.ones(2,2)
tensorA.shape
tensorB=torch.tensor([[1,2,3],[12,5.6,9],[3,5,6]])
print(tensorB)
#así se hace un comentario
print("--------------------------------------")
print("media todo tensorB")
print(torch.mean(tensorB))
print("--------------------------------------")
print("media de cada columna del tensor B")
print(torch.mean(tensorB,dim=0))
print("--------------------------------------")
print("media de cada fila del tensor B")
print(torch.mean(tensorB,dim=1))
print("----------------------------------------------------------------------")
print("desviación estándar del tensor B (para una muestra)")
print(torch.std(tensorB))
print("----------------------------------------------------------------------")
print("desviación estándar de cada columna del tensor B (para una muestra)")
print(torch.std(tensorB, dim=0))
print("----------------------------------------------------------------------")
print("desviación estándar de cada fila del tensor B (para una muestra)")
print(torch.std(tensorB, dim=1))
print("----------------------------------------------------------------------")
url="https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
dataframe=pd.read_csv(url)
dataframe
subset=dataframe[['Overall','Age','International Reputation','Weak Foot','Skill Moves']].dropna(axis=0,how='any')#esto significa que eliminará las filas osea los jugadores que tengan algún valor en NAN o no tengan un numero para este caso...
#cogemos desde el 1 porque no queremos el overall
columns=subset.columns[1:]
players=torch.tensor(subset.values).float()
playersOverall=players[:,0]
meanPlayersOverall=torch.mean(playersOverall)
meanPlayersData=torch.mean(players, dim=0)
stdPlayersData=torch.std(players,dim=0)
norm=(players-meanPlayersData)/torch.sqrt(stdPlayersData)
good=players[torch.ge(playersOverall,85)]
average=players[torch.gt(playersOverall,70) & torch.lt(playersOverall,85)]
notSoGood=players[torch.le(playersOverall,70)]
goodMean=torch.mean(good, dim=0)
averageMean=torch.mean(average, dim=0)
notSoGoodMean=torch.mean(notSoGood, dim=0)
print("media de cada aspecto de todos los jugadores:")
print(meanPlayersData)
print("---------------------------------------------------")
print("promedio de cada jugador:")
print(playersOverall)
print("---------------------------------------------------")
print("media del puntaje general del jugador:")
print(meanPlayersOverall)
print("---------------------------------------------------")
print("Estructura de los datos de los jugadores:")
print(players.shape)
print("---------------------------------------------------")
print("Estructura del puntaje general de los jugadores:")
print(playersOverall.shape)
print("---------------------------------------------------")
print("Datos normalizados:")
print(norm)
print("---------------------------------------------------")
print("media de todos los atributos para los jugadores buenos:")
print(goodMean)
print("---------------------------------------------------")
print("media de todos los atributos para los jugadores promedio:")
print(averageMean)
print("---------------------------------------------------")
print("media de todos los atributos para los jugadores notSoGood:")
print(notSoGoodMean)
for i, args in enumerate(zip(subset, goodMean, averageMean, notSoGoodMean)):
  print('{:25} {:6.2f} {:6.2f} {:6.2f}'.format(*args))