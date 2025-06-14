'''
Clase:        Clase 11
Tema:         Manejo de matrices
Ejercicio:    10.2.1
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Diego Emiliano Romero Castillo
Fecha:        14-06-2025
Estado:       [ Terminado ]
'''


filas = int(input("Número de filas: "))

matriz = []
print("Ingresa cada fila con números separados por coma:")
for i in range(filas):
    fila = input(f"Fila {i + 1}: ")
    numeros = list(map(int, fila.split(',')))
    matriz.append(numeros)

columnas = len(matriz[0])

limite = min(filas, columnas)

diagonal_principal = [matriz[i][i] for i in range(limite)]
diagonal_secundaria = [matriz[i][columnas - 1 - i] for i in range(limite)]

print("Diagonal principal:", diagonal_principal)
print("Diagonal secundaria:", diagonal_secundaria)
