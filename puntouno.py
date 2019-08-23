#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def puntouno(i,j,k):
    z[i][j]=k
    if i==n and j==n:
        return z;
    #el que baja un (i,0)
    elif ((((i+j)%2==0 and i==j) or ((i+j)%2!=0 and i==j+1)) and (i+j<n-1)):
        puntouno(i+j+1,0,k+1)
    #el que baja un (nf-1,i+j+1-n)
    elif (( ((i+j)%2==0 and i==j) or ((i+j)%2!=0 and i==j+1) ) and (i+j>=n-1) and(j<n-1)):
        puntouno(n-1,i+j-n+2,k+1)
    #el que sube
    elif( (((i+j)%2==0 and i>j) or ((i+j)%2!=0 and i>j+1) )):
        puntouno(i-1,j+1,k+1)
# Programa principal
n = int(input("Digite n:"))
z = np.zeros((n, n))
puntouno(0,0,1)
print("\n".join(["".join(["{:4}".format(int(item) if item != 0 else "") for item in row])for row in z]))

