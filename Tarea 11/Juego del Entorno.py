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
    fila = list(map(int, input(f"Fila {numero_fila + 1}: ").split(',')))
    matriz.append(fila)

posiciones_vecinas = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]


matriz_resultado = []

for fila_actual in range(filas):
    nueva_fila = []
    for columna_actual in range(columnas):
        total_vecinos_con_uno = 0

        for desplazamiento_fila, desplazamiento_columna in posiciones_vecinas:
            nueva_fila_vecina = fila_actual + desplazamiento_fila
            nueva_columna_vecina = columna_actual + desplazamiento_columna

            dentro_de_limites = (0 <= nueva_fila_vecina < filas and 0 <= nueva_columna_vecina < columnas)

            if dentro_de_limites:
                if matriz[nueva_fila_vecina][nueva_columna_vecina] == 1:
                    total_vecinos_con_uno += 1

        nueva_fila.append(total_vecinos_con_uno)

    matriz_resultado.append(nueva_fila)

print("Salida:")
for fila in matriz_resultado:
    print(fila)
