consumido = int(input("¿Cuántas unidades consumiste?: "))

if 0 <= consumido <= 100:
    print(f"No debes pagar impuestos, yay!")
elif 101 <= consumido <= 200:
    taxes = consumido*0.5
    total = consumido+taxes
    print(f"Debes pagar en total {total}$ con un impuesto de {taxes}$")
elif consumido >= 201:
    taxes = consumido*0.7
    total = consumido + taxes
    print(f"Debes pagar en total {total}$ con un impuesto de {taxes}$")
else:
    print("Valor consumido no válido, ingrese un valor posible")