import numpy as np 

A=np.array([[2.6,4.8,1.8,0.9],
            [3.2,4.4,2.5,2.8],
            [2.4,3.6,3.8,2.5]])
B=np.array([[3.6,2.5,3.0,2.5],
            [4.5,5.0,3.5,3.8],
            [2.9,3.0,4.6,4.0]])
#indique el orden de la matriz
print(f'el orden de la matriz A {A.shape}')
print()
print(f'el orden de la matriz B {B.shape}')
print()
#calcule la matriz S=A+B
S = A + B
print(f'la suma de las matrices es : \n {S}')
print()
#calcule la matriz D=B-A
D = A - B
print(f'la resta de las matrices es : y queda en D \n {D}')
print()
#indique el valor de los elementos s24 y d24
print(f"el valor de S24 es {S[1][3]}")
print(f"el valor de D24 es {D[1][3]}")
print()
#es posible determinar la matriz t = a+b+e 
print('No se puede calcular ya que la matriz E tienen diferentes dimensiones')
