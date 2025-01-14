import numpy as np 

#ejercicio 1

suma = 0
for n in range(36 ):
    a_n = 200 + 24 * n
    suma += a_n 
    
    print(f'terminoa a{n} = {a_n}')
    print()
    print()
    print(f'el total de lo numeros es {suma}')
    print()
    print()

# ejercicio 2

inicio = 2000000
aumento = 0.012
for i in range(9):
    a_n = inicio * (1+aumento) ** i
    print(f'{i}= {(round(a_n))}')
    print()
    print()

#ejercicio 3

R2 = 1.066  # Rendimiento en el segundo mes
R5 = 8.528  # Rendimiento en el quinto mes
R_n = 34.112  # Rendimiento objetivo

# Calcular la tasa de crecimiento mensual (r)
r = (R5 / R2) ** (1 / 3) - 1  # Raíz cúbica para calcular la tasa de crecimiento

# Inicializamos el mes y el rendimiento en el segundo mes
mes = 2
rendimiento = R2

# Iteramos mes por mes hasta llegar al rendimiento objetivo
while rendimiento < R_n:
    rendimiento *= (1 + r)  # Calculamos el rendimiento para el siguiente mes
    mes += 1  # Incrementamos el mes

# Imprimir el resultado
print("El rendimiento de 34.112 TPS se alcanza en el mes:", mes)
print()


# ejercicio 4

import numpy as np

# Matriz T (unidades producidas y transportadas de planta a bodega)
T = np.array([[300, 272, 240],
              [260, 180, 324]])

# Matriz U (costos de almacenamiento por unidad en cada bodega)
U = np.array([[1200, 1250],  # Bodega 1: enero, febrero
              [1100, 1400],  # Bodega 2: enero, febrero
              [1350, 1200]])  # Bodega 3: enero, febrero

# Calculamos el costo total: multiplicamos T por U
costo_total = np.dot(T, U)

# Mostrar el resultado
print("El costo total de almacenamiento para cada mes (enero y febrero) es:")
print()
print(costo_total)