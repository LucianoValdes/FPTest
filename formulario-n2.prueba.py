import numpy as np 

#EJERCICIO 1
sum = 0
for n in range(36):
    i_n = 200 + 24 * n
    sum += i_n
    print(f'Los valores de los terminos son a{n}={i_n}')
    
print()   
print(f'La suma de los primeros 36 numeros es {sum}')

#EJERCICIO 2
print()
Inicio = 2000000
PO = 0.012
for n in range(1,10):
    F_M = Inicio * (1+PO) ** n 
    print(f'esto es lo que a aumentado el interes de la cuenta de ahorros a{n}={(round(F_M))}')

#EJERCICIO 3


# Crear la matriz A (3x3) usando la expresión a_ij = 2*i + 3*j
A = np.array([[2*i + 3*j for j in range(1, 4)] for i in range(1, 4)])

# Crear la matriz B (3x3) usando la expresión b_ij = 10*i*j
B = np.array([[10*i*j for j in range(1, 4)] for i in range(1, 4)])

# Calcular el producto de las matrices A y B
C = np.dot(A, B)

# Mostrar las matrices
print("Matriz A:")
print(A)

print("Matriz B:")
print(B)

print("Matriz C (A * B):")
print(C)
print()
 #EJERCICIO 4 

T=np.array([[300,272,240],
            [260,180,324]])
U=np.array([[1200,1250],
           [1100,1400],
           [1350,1200]])
Ñ=np.dot(T,U)
print(f'el costo de almacenar en la planta dos fue de {Ñ[1]+[0,1]}')
print()

#EJERCICIO 5

S=np.array([[360,280,150,420],
            [450,370,210,130],
            [240,260,320,340]])
C=np.array([[130,310,230,280],
            [270,240,520,370],
            [190,290,460,410]])
A= S + C
print(f'a12 nos indica que es el producto 1 del modelo 2 es:{A}\n {A[0][1]}')
print()

P_SA=S[1][2]*0.80
P_CO=C[1][2]*1.10
TOTAL = P_SA + P_CO
print('La produccion total es ', round(TOTAL))
print()

#EJERCICIO 6 

M = np.fromfunction(lambda i, j: 2*(i+1) + 3*(j+1), (3,3))
print(M)
V = np.fromfunction(lambda i, j: 10*(i+1) * (j+1), (3,3))
J=np.dot(M,V)
print(V)
print(f'la matriz j{J}')



#EJERCICIO 7
A = np.array([[2, 3], [1, 4]])
B = np.array([52, 56])
resultados = np.linalg.solve(A, B)
print(resultados)
print(f"El Software A debe operar {resultados[0]} minutos.")
print(f"El Software B debe operar {resultados[1]} minutos.")




 
    