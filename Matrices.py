import numpy as np 

#MATRICES 
#SUMA DE MATRICES
E_1 = np.array([[8, 2, 1],
[-5, 6, 7]])
F_2 = np.array([[3, 4, 0],
[4, -3, 9]])

suma = E_1 + F_2
print(suma)                     #LO MISMO PARA RESTAR



#definir matriz por funcion 
M = np.fromfunction(lambda i, j: (i+1) + (j+1), (2,2))
print(M)

