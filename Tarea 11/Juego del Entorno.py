'''
Clase:        Clase 11
Tema:         Manejo de matrices
Ejercicio:    10.3.2
Descripción:  Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).

Autor:        Diego Emiliano Romero Castillo
Fecha:        14-06-2025
Estado:       [ Terminado ]
'''

filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

print("Ingresa la matriz (una fila por línea, con números separados por coma):")
matriz = []
for numero_fila in range(filas):
    while True:
        fila = list(map(int, input(f"Fila {numero_fila + 1}: ").split(',')))
        if len(fila) == columnas:
            matriz.append(fila)
            break
        else:
            print(f"Error: se esperaban {columnas} valores. Intenta nuevamente.")

# Definición de posiciones vecinas (8 direcciones)
posiciones_vecinas = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

matriz_resultado = []

for fila_actual in range(filas):
    nueva_fila = []
    for columna_actual in range(columnas):
        total_vecinos_con_uno = 0

        for df, dc in posiciones_vecinas:
            nf, nc = fila_actual + df, columna_actual + dc
            if 0 <= nf < filas and 0 <= nc < columnas:
                if matriz[nf][nc] == 1:
                    total_vecinos_con_uno += 1

        nueva_fila.append(total_vecinos_con_uno)
    matriz_resultado.append(nueva_fila)

print("Salida:")
for fila in matriz_resultado:
    print(fila)
