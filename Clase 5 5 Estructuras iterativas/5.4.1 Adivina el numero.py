import random
magico = random.randint(1,100)
x = True
while x == True:
    intento = int(input("Ingresa un numero entre 1 y 100: "))
    if intento == magico:
        x = False
        print(f"¡Felicidades! Has adivinado el número secreto: {magico}")
        print("Fin del juego")
    elif intento > magico:
        print("El número secreto es menor")
    else:
        print("El número secreto es mayor")