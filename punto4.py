#!/usr/bin/env python
# coding: utf-8
# In[5]:
import numpy as np
def puntocuatro(i,j,k):
    print(i,j,k)
    z[i][j]=k
    k=k+1
    if j==int(n/2) and i==int(n/2):
        return z
    elif j==int(n/2) and i<=(int(n/2)-1):#singularidades
        puntocuatro(j,n-i-2,k)
    elif j==int(n/2) and i>(int(n/2)-1):#singularidades
        puntocuatro(int(n/2)-1,n-i,k)
    elif j>int(n/2) and i>=int(n/2):#bajando por la derecha llamado recursivo pequeño
        z[i][n-j-1]=k
        puntocuatro(i+1,j-1,k+1)
    elif i<int(n/2) and j<int(n/2):#subiendo por la izquierda llamado recursivo pequeño
        z[i][n-j-1]=k
        puntocuatro(i-1,j+1,k+1) 
#principal
n = int(input("Digite n:"))
z = np.zeros((n, n))
puntocuatro(int(n/2),n-1,1)
print("\n".join(["".join(["{:4}".format(int(item) if item != 0 else "") for item in row])for row in z]))

