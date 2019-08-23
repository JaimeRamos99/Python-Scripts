#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
def puntodos(i,j,k): 
    if k>=int(n/2)**2+2*int(n/2)+2:#caso base
          return z
    elif j<int(n/2) and (i>=0):#SUBIENDO
        z[i][j]=k
        if(j>0):
            k=k+1
            z[n-1-i-j][j]=k
        if(i>0):
            puntodos(i-1,j+1,k+1)
    elif j>=int(n/2) and (i<=int(n/2)):#BAJANDO
        z[i][j]=k
        k=k+1
        if j-i==i and k<int(n/2)**2+2*int(n/2)+2:##mando a izquierda de nuevo      
            z[i-1][n-j+1]=k
            puntodos(i-2,n-j+2,k+1)
        elif(j<n-1) and k<int(n/2)**2+2*int(n/2)+2:#el que baja normal
            z[j-i][j]=k
            puntodos(i+1,j+1,k+1)
# Programa principal
n = int(input("Digite n:"))
z = np.zeros((int(n/2)+2, n))
puntodos(int(n/2),0,1)
print("\n".join(["".join(["{:4}".format(int(item) if item != 0 else "") for item in row])for row in z]))

