'''
Clase:        Clase 11
Tema:         Manejo de matrices
Ejercicio:    10.3.1
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.

Autor:        Diego Emiliano Romero Castillo
Fecha:        2025-14-26
Estado:       [ Terminado ]
'''

n = int(input("Ingresa la dimensión de la matriz: "))

matriz = []
print(f"Ingrese {n} filas de números separados por coma:")
for i in range(n):
    fila = input(f"Fila {i + 1}: ")
    numeros = list(map(int, fila.split(',')))
    matriz.append(numeros)

es_simetrica = True 

for i in range(n):
    for j in range(i + 1, n):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False
            break
    if not es_simetrica:
        break

if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
