# me dan una lista
# lista 2
# para cada elemento de la lista 1 checo si hay un numero mayor a partir de su indice +1 en la lista 1
    # si no hay ninguno, entonces lo agrego a una lista "lider"


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

print(lideres)