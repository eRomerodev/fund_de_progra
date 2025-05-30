'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    6.3.1
Descripción:  Dada una lista por el usuario, tomando cada numero, si los numeros que tiene a la derecha todos son menores, entonces es "lider" regresa los numeros lideres

Autor:        Diego Emiliano Romero Castillo
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

lista = input("Dame una lista: ")

liston = lista.split()
def integer(x):
    return int(x)

lista1 = list(map(integer,liston))
lista2 = lista1
lideres = []

hola = True

for i in lista1:
    for j in lista2[i:]:
        if i > j:
            hola = True
        else:
            hola = False
            pass
    if hola == True:
        lideres.append(i)

print(*lideres)