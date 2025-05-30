# pedir un número al usuario
# si el numero tiene un solo digito
    # imprimir "El resultado final es {digito}"
# cualquier otra cantidad de digitos:
    # hacer el numero una lista
    # hacer cada item numeric
    # sumar cada item y asignarlo a una variable
    # si esa variable es >= 10
        # repetir todo lo anterior
    # si la variable es cualquier otro valor:
        #imprimir "El resultado final es {digito}"

def integer(str):
    return int(str)

numero = int(input("Ingresa un número: "))
print(" ")

if numero < 10:
    print(f"El resultado final es {numero}")
else:
    print(f"Proceso de reducción para {numero}:")
    largo = True
    while largo == True:
        string = str(numero)
        lista = list(string)
        nums = map(integer,lista)
        sumita = sum(i for i in nums)
        print(f"{numero} = {sumita}")
        if sumita >= 10:
            numero = sumita
            largo = True
        else:
            print(" ")
            print(f"El resultado final es: {sumita}")
            largo = False