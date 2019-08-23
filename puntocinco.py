import numpy as np
def clase(i,j,k):#para numeros pares
    z[i][j]=k
    if j==v and i==int((n-2)/2):
        return z
    elif i==n-2 and j<v:##singularidad 1
        clase(j,int((n-2)/2)+1,k+1)
    elif j==v and i>=v:##singularidad 2
        clase(0,n-i-1,k+1)
    elif j<v:
        clase(i+1,j,k+1)
    elif j>=v and i<int((n-2)/2):
         clase(i+1,j+1,k+1)
    elif j>=v and i>=int((n-2)/2): 
        clase(i+1,j-1,k+1)
#principal
n = int(input("Digite n:"))
v=int(n/2)
z = np.zeros((n, n+1))
clase(0,0,1)
print("\n".join(["".join(["{:4}".format(int(item) if item != 0 else "") for item in row])for row in z]))