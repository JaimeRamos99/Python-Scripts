#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np 
def puntotres(i,j,k):
    z[i][j]=k
    if i+j==0:
        return z
    elif (((i+j)%2==0 and i==0)or ((i+j)%2!=0 and i==nf-1 and j>0)):
                puntotres(i,j-1,k+1)
    elif ((i+j)%2==0 and j==nc-1)or((i+j)%2!=0 and j==0):
                puntotres(i-1,j,k+1)
    elif((i+j)%2==0):
                puntotres(i-1,j+1,k+1)
    elif((i+j)%2!=0):
                 puntotres(i+1,j-1,k+1)
#programa principal          
nf = int(input("Digite el número de filas:"))
nc = int(input("Digite el número de columnas:"))
z = np.zeros((nf,nc))
puntotres(nf-1,nc-1,1)
print("\n".join(["".join(["{:4}".format(int(item) if item != 0 else "") for item in row])for row in z]))
