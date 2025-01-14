import numpy as np

T=np.array([[300,272,240],
            [260,180,324]])
U=np.array([[1200,1250],
            [1100,1400],
            [1350,1200]])

F=np.dot(T,U)
print(F)
print()

#ejercicio12,formulario 2
S = [
    [360, 280, 150, 420],
    [450, 370, 210, 130],
    [240, 260, 320, 340]
]

C = [
    [130, 310, 230, 280],
    [270, 240, 520, 370],
    [190, 290, 460, 410]
]

# Cálculo de la producción proyectada para el modelo 3 del producto 2
produccion_santiago = S[1][2] * 0.80  # 20% menos en Santiago
produccion_concepcion = C[1][2] * 1.10  # 10% más en Concepción

# Producción total proyectada
produccion_total = produccion_santiago + produccion_concepcion

# Mostrar el resultado
print("Producción estimada para el modelo 3 del producto 2:", round(produccion_total))
print()

A = np.array([[2, 1], [3, -2]])  # Coeficientes de las variables (x y)
B = np.array([10, 8])  # Términos constantes del sistema

# Resolver el sistema de ecuaciones
solucion = np.linalg.solve(A, B)

# Mostrar los resultados
print(f"Minutos que debe ejecutarse el Servicio A (x): {solucion[0]}")
print(f"Minutos que debe ejecutarse el Servicio B (y): {solucion[1]}")

print()
A=np.array([[2,3],
           [1,2]])
I=A.T
suma = A + I
print(I)
print(suma)
print()
print()








# Definir las matrices de coeficientes y los términos constantes
A = np.array([[2, 3], 
              [1, 4]])  # Coeficientes de las variables (x y)
B = np.array([52, 56])  # Términos constantes del sistema

# Resolver el sistema de ecuaciones
solucion = np.linalg.solve(A, B)

# Mostrar los resultados
print(f"Minutos que debe ejecutarse el Servicio A (x): {solucion[0]}")
print(f"Minutos que debe ejecutarse el Servicio B (y): {solucion[1]}")